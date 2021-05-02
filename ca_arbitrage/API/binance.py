import hashlib
import hmac
import time
import requests
import json


class BinanceAPI:

    def __init__(self, api_key='', api_secret=''):
        self.baseurl = 'https://api.binance.com/api/'
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self):
        session = requests.session()
        session.headers.update({'Accept': 'application/json',
                                'User-Agent': 'binance/python',
                                'X-MBX-APIKEY': self.api_key})
        return session

    def graph(self, quote, base):
        ticks = self._request("v3/klines", {'symbol': base + quote, 'interval': '1d'})
        x = []
        y = []
        if 'code' in ticks:
            return []
        for tick in ticks:
            x.append({
                'x': tick[0],
                'y': float(tick[4])
            })
            y.append({
                'x': tick[0],
                'y': float(tick[5])
            })
        return [x, y]

    def pricesdata(self):
        arr = self._prices()
        array = {}
        if 'code' not in array and arr:
            for obj in arr:
                array[obj['symbol']] = {
                    'prices': obj['lastPrice'],
                    'bid': obj['bidPrice'],
                    'ask': obj['askPrice'],
                    'volume': obj['quoteVolume']
                }
        return array

    def parsebalance(self):
        arr = self._account()
        array = {}

        if 'code' not in arr and arr:
            prices = self.pricesdata()
            for key in arr['balances']:
                if float(key['free']) + float(key['locked']) > 0:
                    btc = (float(key['free']) + float(key['locked'])) if key['asset'] == 'BTC' \
                        else ((float(key['free']) + float(key['locked'])) / float(prices['BTCUSDT']['prices'])
                              if key['asset'] == 'USDT'
                              else ((float(key['free']) + float(key['locked'])) * float(
                        prices[key['asset'] + 'BTC']['prices']) if key['asset'] + 'BTC' in prices else 0))
                    price = (float(key['free']) + float(key['locked'])) if key['asset'] == 'USDT' \
                        else btc * float(prices['BTCUSDT']['prices'])
                    array[key['asset']] = {
                        'amount': float(key['free']) + float(key['locked']),
                        'totalbtc': btc,
                        'totalusd': price
                    }

        return array

    def _timestamp(self):
        return self._request("v3/time")['serverTime']

    def _account(self):
        return self._signed_request("v3/account")

    def _prices(self):
        return self._request("v3/ticker/24hr")

    def _request(self, func, parameters=None):
        url = self.baseurl + func
        if parameters:
            url += '?'
            for k, v in parameters.items():
                url += str(k) + '=' + str(v) + '&'
            url = url[:-1]
        return json.loads(requests.get(url).text)

    def _signed_request(self, url, parameters=None):
        if parameters is None:
            parameters = {}
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        # parameters['timestamp'] = int(time.time() * 1000)
        parameters['timestamp'] = self._timestamp()

        query = ''
        if parameters:
            for k, v in parameters.items():
                query += str(k) + '=' + str(v) + '&'
            query = query[:-1]

        signature = hmac.new(self.api_secret.encode('utf-8'), query.encode('utf-8'), hashlib.sha256).hexdigest()
        endpoint = self.baseurl + url + '?' + query + '&signature=' + signature

        request = self._init_session()
        response = request.get(endpoint).text
        return json.loads(response)
