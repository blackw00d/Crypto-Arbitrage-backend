import base64
import hashlib
import hmac
import time
import urllib.parse
import requests
import json


class KucoinAPI:

    def __init__(self, api_key='', api_secret='', password=''):
        self.baseurl = ' https://api.kucoin.com'
        self.api_key = api_key
        self.api_secret = api_secret
        self.password = password

    def _init_session(self, timestamp, signature, password):
        session = requests.session()
        session.headers.update(
            {
                "KC-API-SIGN": signature,
                "KC-API-TIMESTAMP": str(timestamp),
                "KC-API-KEY": self.api_key,
                "KC-API-PASSPHRASE": password,
                "Content-Type": "application/json",
                "KC-API-KEY-VERSION": "2"
            }
        )
        return session

    def graph(self, quote, base):
        url = self.baseurl + '/api/v1/market/candles?type=1day&symbol=' + base + "-" + quote
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['code'] != "200000":
            return []
        for tick in ticks['data']:
            x.append({
                'x': int(tick[0]) * 1000,
                'y': float(tick[2])
            })
            y.append({
                'x': int(tick[0]) * 1000,
                'y': float(tick[6])
            })
        return [x, y]

    def parsebalance(self):
        arr = self._account()
        array = {}

        if arr and 'code' in arr:
            if arr['code'] == '200000':
                prices = self.pricesdata()

                for key in arr['data']:
                    if float(key['balance']) > 0:
                        btc = float(key['balance']) if key['currency'] == 'BTC' \
                            else (float(key['balance']) / float(prices['BTC-USDT']['prices'])
                                  if key['currency'] == 'USDT'
                                  else (float(key['balance']) * float(prices[key['currency'] + '-BTC']['prices'])
                                        if key['currency'] + '-BTC' in prices else 0))
                        price = float(key['balance']) if key['currency'] == 'USDT' \
                            else btc * float(prices['BTC-USDT']['prices'])
                        array[key['currency']] = {
                            'amount': array[key]['amount'] + float(key['balance']) if key['currency'] in array
                            else float(key['balance']),
                            'totalbtc': array[key]['totalbtc'] + btc if key['currency'] in array else btc,
                            'totalusd': array[key]['totalusd'] + price if key['currency'] in array else price
                        }

        return array

    def pricesdata(self):
        url = self.baseurl + "/api/v1/market/allTickers"
        arr = json.loads(requests.get(url).text)
        array = {}

        if arr and 'code' in arr:
            if arr['code'] == '200000':
                for obj in arr['data']['ticker']:
                    array[obj['symbol']] = {
                        'prices': obj['last'],
                        'bid': obj['buy'],
                        'ask': obj['sell']
                    }
        return array

    def _account(self):
        return self._signed_request("/api/v1/accounts")

    def _signed_request(self, url, method='GET', parameters=None):
        if parameters is None:
            parameters = {}
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        timestamp = int(time.time()) * 1000
        if parameters and len(parameters):
            if method in ['GET', 'DELETE']:
                url += '?' + '&'.join(['%s=%s' % (key, urllib.parse.quote(parameters[key], safe=''))
                                       for key in sorted(parameters.keys())])
            else:
                url += json.dumps(parameters)

        presign = ''.join([str(timestamp), method, url])
        signature_sha256 = hmac.new(self.api_secret.encode('utf-8'), presign.encode('utf-8'), hashlib.sha256).digest()
        signature = base64.b64encode(signature_sha256).decode()

        password_sha256 = hmac.new(self.api_secret.encode('utf-8'), self.password.encode('utf-8'),
                                   hashlib.sha256).digest()
        password = base64.b64encode(password_sha256).decode()

        request = self._init_session(timestamp, signature, password)
        if method in ['GET', 'DELETE']:
            response = request.get(self.baseurl + url).text
        else:
            response = request.post(self.baseurl + url, json.dumps(parameters)).text
        return json.loads(response)
