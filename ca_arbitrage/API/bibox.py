import hashlib
import hmac
import time
import requests
import json


class BiboxAPI:

    def __init__(self, api_key='', api_secret=''):
        self.baseurl = 'https://api.bibox.com'
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self, signature, timestamp):
        session = requests.session()
        session.headers.update(
            {
                'content-type': 'application/json',
                'bibox-api-key': self.api_key,
                'bibox-timestamp': str(timestamp),
                'bibox-api-sign': signature
            }
        )
        return session

    def graph(self, quote, base):
        url = self.baseurl + '/v3/mdata/kline?pair=' + base + "_" + quote + '&period=day'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['state'] != 0:
            return []
        for tick in ticks['result']:
            x.append({
                'x': tick['time'],
                'y': float(tick['close'])
            })
            y.append({
                'x': tick['time'],
                'y': float(tick['vol'])
            })
        return [x, y]

    def parsebalance(self):
        arr = self._account()
        array = {}

        if arr and 'state' in arr:
            if arr['state'] == '0':
                for key in arr['result']:
                    array[key['coin_symbol']] = {
                        'amount': key['balance'] + key['freeze'],
                        'totalbtc': key['BTCValue'],
                        'totalusd': key['USDValue']
                    }

        return array

    def pricesdata(self):
        url = self.baseurl + "v3/mdata/marketAll"
        arr = json.loads(requests.get(url).text)
        array = {}

        if arr and 'state' in arr:
            if arr['state'] == 0:
                for key in arr['result']:
                    array[key['coin_symbol'] + key['currency_symbol']] = {
                        'prices': key['last']
                    }
        return array

    def _account(self):
        return self._signed_request("/v3.1/transfer/mainAssets", {'select': 1})

    def _signed_request(self, url, parameters=None):
        if parameters is None:
            parameters = {}
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        timestamp = int(time.time()) * 1000
        body = json.dumps(parameters)
        presign = str(timestamp) + body
        signature = hmac.new(self.api_secret.encode('utf-8'), presign.encode('utf-8'), hashlib.md5).hexdigest()

        request = self._init_session(signature, timestamp)
        response = request.post(self.baseurl + url, body).text
        return json.loads(response)
