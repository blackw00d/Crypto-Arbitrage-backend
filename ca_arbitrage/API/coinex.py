import hashlib
import time
import urllib.parse
import requests
import json


class CoinexAPI:

    def __init__(self, api_key='', api_secret=''):
        self.baseurl = 'https://api.coinex.com'
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self, signature):
        session = requests.session()
        session.headers.update(
            {
                'authorization': signature
            }
        )
        return session

    def graph(self, quote, base):
        url = self.baseurl + '/v1/market/kline?market=' + base + quote + '&type=1day'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['code'] != 0:
            return []
        for tick in ticks['data']:
            x.append({
                'x': tick[0] * 1000,
                'y': float(tick[2])
            })
            y.append({
                'x': tick[0] * 1000,
                'y': float(tick[5])
            })
        return [x, y]

    def parsebalance(self):
        arr = self._account()
        array = {}

        if arr and 'code' in arr:
            if arr['code'] == '0':
                prices = self.pricesdata()
                for key, value in arr['data'].items():
                    balance = float(value['available']) + float(value['frozen'])
                    if balance > 0:
                        btc = balance if key == 'BTC' \
                            else (balance / float(prices['BTCUSDT']['prices'])
                                  if key == 'USDT'
                                  else (balance * float(prices[key + 'BTC']['prices']) if key + 'BTC' in prices else 0))
                        price = balance if key == 'USDT' else btc * float(prices['BTCUSDT']['prices'])
                        array[key] = {
                            'amount': balance,
                            'totalbtc': btc,
                            'totalusd': price
                        }

        return array

    def pricesdata(self):
        url = self.baseurl + "/v1/market/ticker/all"
        arr = json.loads(requests.get(url).text)
        array = {}

        if arr and 'code' in arr:
            if arr['code'] == 0:
                for key, value in arr['data']['ticker'].items():
                    array[key] = {
                        'prices': value['last'],
                        'bid': value['buy'],
                        'ask': value['sell']
                    }
        return array

    def _account(self):
        return self._signed_request("/v1/balance/info")

    def _signed_request(self, url, method='GET', parameters=None):
        if parameters is None:
            parameters = {}
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        timestamp = int(time.time()) * 1000
        parameters.update({
            'access_id': self.api_key,
            'tonce': str(timestamp)
        })
        parameters = dict(sorted(parameters.items()))
        body = '&'.join(['%s=%s' % (key, urllib.parse.quote(parameters[key], safe=''))
                         for key in sorted(parameters.keys())])

        presign = body + '&secret_key=' + self.api_secret
        signature = hashlib.md5(presign.encode()).hexdigest().upper()

        request = self._init_session(signature)
        if method == 'GET':
            response = request.get(self.baseurl + url + '?' + body).text
        else:
            response = request.post(self.baseurl + url, parameters).text
        return json.loads(response)
