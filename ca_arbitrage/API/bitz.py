import hashlib
import time
import random
import requests
import json


class BitZAPI:

    def __init__(self, api_key='', api_secret=''):
        self.baseurl = 'https://apiv2.bitz.com'
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self, timestamp, nonce, signature):
        session = requests.session()
        session.headers.update(
            {
                'apiKey': self.api_key,
                'timeStamp': timestamp,
                'nonce': nonce,
                'sign': signature
            }
        )
        return session

    def graph(self, quote, base):
        url = self.baseurl + '/Market/kline?symbol=' + base.lower() + '_' + quote.lower() + '&resolution=1day'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['status'] != 200:
            return []
        for tick in ticks['data']['bars']:
            x.append({
                'x': int(tick['time']),
                'y': float(tick['close'])
            })
            y.append({
                'x': int(tick['time']),
                'y': float(tick['volume'])
            })
        return [x, y]

    def parsebalance(self):
        arr = self._account()
        array = {}

        if arr and 'status' in arr:
            if arr['status'] == 200:
                if arr['data']['info']:
                    for key in arr['data']['info']:
                        if float(key['num']) > 0:
                            array[key.upper()] = {
                                'amount': float(key['num']),
                                'totalbtc': key['btc'],
                                'totalusd': key['usd']
                            }

        return array

    def pricesdata(self):
        url = self.baseurl + "/Market/tickerall"
        arr = json.loads(requests.get(url).text)
        array = {}
        if arr and 'status' in arr:
            if arr['status'] == 200:
                for obj in arr['data'].values():
                    array[obj['symbol']] = {
                        'prices': obj['now'],
                        'bid': obj['bidPrice'],
                        'ask': obj['askPrice']
                    }
        return array

    def _account(self):
        return self._signed_request("/Assets/getUserAssets")

    def _signed_request(self, url, parameters=None):
        if parameters is None:
            parameters = {}
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        timestamp = str(int(time.time()))
        nonce = str(random.randint(100000, 999999))

        header = {
            'apiKey': self.api_key,
            'timeStamp': timestamp,
            'nonce': nonce,
        }
        if parameters and len(parameters):
            for key, value in parameters.items():
                header.update({key: value})

        body = '&'.join(['%s=%s' % (key, header[key]) for key in sorted(header.keys())])
        data = "%s%s" % (body, self.api_secret)
        signature = hashlib.md5(data.encode("utf8")).hexdigest().lower()
        header.update({'sign': signature})

        url = self.baseurl + url
        request = self._init_session(timestamp, nonce, signature)
        response = request.post(url, header).text
        return json.loads(response)
