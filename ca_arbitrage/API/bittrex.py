import hashlib
import hmac
import time
from datetime import datetime
import requests
import json


class BittrexAPI:

    def __init__(self, api_key='', api_secret=''):
        self.baseurl = 'https://api.bittrex.com/'
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self, timestamp, content_hash, signature):
        session = requests.session()
        session.headers.update(
            {
                'Api-Timestamp': str(timestamp),
                'Api-Key': self.api_key,
                'Content-Type': 'application/json',
                'Api-Content-Hash': content_hash,
                'Api-Signature': signature
            }
        )
        return session

    def graph(self, quote, base):
        url = self.baseurl + "v3/markets/" + base + "-" + quote + "/candles/TRADE/DAY_1/recent"
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if 'code' in ticks:
            return []
        for tick in ticks:
            x.append({
                'x': int(datetime.strptime(tick['startsAt'], '%Y-%m-%dT%H:%M:%SZ').timestamp() * 1000),
                'y': float(tick['close'])
            })
            y.append({
                'x': int(datetime.strptime(tick['startsAt'], '%Y-%m-%dT%H:%M:%SZ').timestamp() * 1000),
                'y': float(tick['quoteVolume'])
            })
        return [x, y]

    def parsebalance(self):
        arr = self._account()
        array = {}

        if 'code' not in arr and arr:
            prices = self.pricesdata()
            for key in arr:
                if float(key['total']) > 0:
                    btc = float(key['total']) if key['currencySymbol'] == 'BTC' \
                        else (float(key['total']) / float(prices['BTC-USDT']['prices'])
                              if key['currencySymbol'] == 'USDT'
                              else (float(key['total']) * float(prices[key['currencySymbol'] + '-BTC']['prices'])
                                    if key['currencySymbol'] + '-BTC' in prices else 0))
                    price = float(key['total']) if key['currencySymbol'] == 'USDT' \
                        else btc * float(prices['BTC-USDT']['prices'])
                    array[key['currencySymbol']] = {
                        'amount': float(key['total']),
                        'totalbtc': btc,
                        'totalusd': price
                    }

        return array

    def pricesdata(self):
        url = self.baseurl + "v3/markets/tickers"
        arr = json.loads(requests.get(url).text)
        array = {}
        if 'code' not in array and arr:
            for obj in arr:
                array[obj['symbol']] = {
                    'prices': obj['lastTradeRate'],
                    'bid': obj['bidRate'],
                    'ask': obj['askRate']
                }
        return array

    def _account(self):
        return self._signed_request("v3/balances")

    def _signed_request(self, url, method='GET', parameters=None):
        if parameters is None:
            parameters = {}
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        url = self.baseurl + url
        timestamp = int(time.time() * 1000)
        content = ''
        if parameters:
            content = json.dumps(parameters)

        content_hash = hashlib.sha512(content.encode('utf-8')).hexdigest()
        presign = ''.join([str(timestamp), url, method, content_hash])
        signature = hmac.new(self.api_secret.encode('utf-8'), presign.encode('utf-8'), hashlib.sha512).hexdigest()

        request = self._init_session(timestamp, content_hash, signature)
        response = request.get(url).text
        return json.loads(response)
