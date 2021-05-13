import hashlib
import hmac
import time
import requests
import json


class GateIOAPI:

    def __init__(self, api_key='', api_secret=''):
        self.base = 'https://api.gateio.ws'
        self.prefix = '/api/v4'
        self.baseurl = self.base + self.prefix
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self, timestamp, signature):
        session = requests.session()
        session.headers.update(
            {
                'KEY': self.api_key,
                'Timestamp': str(timestamp),
                'SIGN': signature
            }
        )
        return session

    def graph(self, quote, base):
        url = self.baseurl + '/spot/candlesticks?currency_pair=' + base + "_" + quote + '&interval=1d'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if 'label' in ticks:
            return []
        for tick in ticks:
            x.append({
                'x': int(tick[0]) * 1000,
                'y': float(tick[2])
            })
            y.append({
                'x': int(tick[0]) * 1000,
                'y': float(tick[1])
            })
        return [x, y]

    def parsebalance(self):
        arr = self._account()
        array = {}

        if 'label' not in arr and arr:
            prices = self.pricesdata()
            for key in arr:
                if 'available' in key:
                    for value in key:
                        if float(key[value]) > 0:
                            btc = float(key[value]) if value == 'BTC' \
                                else (float(key[value]) / float(prices['BTCUSD']['prices'])
                                      if value == 'USD'
                                      else (float(key[value]) * float(prices[value + '_BTC']['prices'])
                                            if value + '_BTC' in prices else 0))
                            price = float(key[value]) if value == 'USD' else btc * float(prices['BTCUSD']['prices'])
                            array[value] = {
                                'amount': float(key[value]),
                                'totalbtc': btc,
                                'totalusd': price
                            }

        return array

    def pricesdata(self):
        url = self.baseurl + "/spot/tickers"
        arr = json.loads(requests.get(url).text)
        array = {}
        if 'label' not in array and arr:
            for obj in arr:
                array[obj['currency_pair']] = {
                    'prices': obj['last'],
                    'bid': obj['highest_bid'],
                    'ask': obj['lowest_ask']
                }
        return array

    def _account(self):
        return self._signed_request("/wallet/sub_account_balances")

    def _signed_request(self, url, method='GET', parameters=None):
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        body = ''
        if parameters and len(parameters):
            body = json.dumps(parameters)

        timestamp = int(time.time())
        body = hashlib.sha512(body.encode('utf-8')).hexdigest()
        pre_sign = '%s\n%s\n%s\n%s\n%s' % (method, self.prefix + url, '', body, timestamp)
        signature = hmac.new(self.api_secret.encode('utf-8'), pre_sign.encode('utf-8'), hashlib.sha512).hexdigest()

        request = self._init_session(timestamp, signature)
        response = request.get(self.baseurl + url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return {}
