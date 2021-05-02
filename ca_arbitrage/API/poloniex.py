import hashlib
import hmac
import json
import time
import requests


class PoloniexAPI:

    def __init__(self, api_key='', api_secret=''):
        self.public = 'https://poloniex.com/public'
        self.trading = 'https://poloniex.com/tradingApi'
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self, signature):
        session = requests.session()
        session.headers.update(
            {
                "Key": self.api_key,
                "Sign": signature
            }
        )
        return session

    def graph(self, quote, base):
        url = self.public + '?command=returnChartData&currencyPair=' + quote + "_" + base + \
              '&start=1325376000&end=9999999999&period=86400'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if 'error' in ticks:
            return []
        for tick in ticks:
            x.append({
                'x': tick['date'] * 1000,
                'y': tick['close']
            })
            y.append({
                'x': tick['date'] * 1000,
                'y': tick['quoteVolume']
            })
        return [x, y]

    def pricesdata(self):
        arr = self._prices()
        array = {}

        if 'error' not in array and arr:
            for key, value in arr.items():
                array[key] = {
                    'prices': value['last'],
                    'bid': value['highestBid'],
                    'ask': value['lowestAsk'],
                    'volume': value['quoteVolume']
                }
        return array

    def parsebalance(self):
        arr = self._account()
        array = {}

        if 'error' not in arr and arr:
            prices = self.pricesdata()

            for key, value in arr.items():
                if float(value) > 0:
                    btc = float(value) if key == 'BTC' \
                        else (float(value) / float(prices['USDT_BTC']['prices'])
                              if key == 'USDT'
                              else (float(value) * float(prices['BTC_' + key]['prices'])
                                    if 'BTC_' + key in prices else 0))
                    price = float(value) if key == 'USDT' \
                        else btc * float(prices['USDT_BTC']['prices'])
                    array[key] = {
                        'amount': float(value),
                        'totalbtc': btc,
                        'totalusd': price
                    }

        return array

    def _prices(self):
        url = self.public + '?command=returnTicker'
        return json.loads(requests.get(url).text)

    def _account(self):
        return self._signed_request({'command': 'returnBalances'})

    def _signed_request(self, parameters=None):
        if parameters is None:
            parameters = {}
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        nonce = int(time.time() * 1000000)
        parameters.update({'nonce': nonce})

        body = ''
        if parameters:
            for k, v in parameters.items():
                body += str(k) + '=' + str(v) + '&'
            body = body[:-1]

        signature = hmac.new(self.api_secret.encode('utf-8'), body.encode('utf-8'), hashlib.sha512).hexdigest()

        request = self._init_session(signature)
        response = request.post(self.trading, parameters).text
        return json.loads(response)
