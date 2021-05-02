import urllib.parse
import requests
from requests.auth import AuthBase
from urllib.parse import urlparse
from base64 import b64encode
import hmac
import hashlib
import time
from datetime import datetime
import json


class HS256(AuthBase):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self, r):
        url = urlparse(r.url)
        timestamp = str(int(time.time()))
        msg = r.method + timestamp + url.path
        if url.query != "":
            msg += "?" + url.query
        if r.body:
            msg += r.body

        signature = hmac.new(self.password.encode(), msg.encode(), hashlib.sha256).hexdigest()
        authstr = "HS256 " + b64encode(
            b':'.join((self.username.encode(), timestamp.encode(), signature.encode()))).decode().strip()

        r.headers['Authorization'] = authstr
        return r


class HitBTCAPI:

    def __init__(self, api_key='', api_secret=''):
        self.baseurl = 'https://api.hitbtc.com/api/'
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self):
        session = requests.session()
        session.auth = HS256(self.api_key, self.api_secret)
        return session

    def graph(self, quote, base):
        url = self.baseurl + '2/public/candles/' + base + quote + '?period=Ds1'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if 'status' in ticks:
            return []
        for tick in ticks:
            x.append({
                'x': int(datetime.strptime(tick['timestamp'], '%Y-%m-%dT%H:%M:%S.000Z').timestamp() * 1000),
                'y': float(tick['close'])
            })
            y.append({
                'x': int(datetime.strptime(tick['timestamp'], '%Y-%m-%dT%H:%M:%S.000Z').timestamp() * 1000),
                'y': float(tick['volumeQuote'])
            })
        return [x, y]

    def parsebalance(self):
        arr = self._account()
        array = {}

        if 'error' not in arr and arr:
            prices = self.pricesdata()
            for key in arr:
                price = float(key['available']) + float(key['reserved'])
                if price > 0:
                    btc = price if key['currency'] == 'BTC' \
                        else (price / float(prices['BTCUSD']['prices'])
                              if key['currency'] == 'USD'
                              else (price * float(prices[key['currency'] + 'BTC']['prices'])
                                    if key['currency'] + 'BTC' in prices else 0))
                    price = price if key['currency'] == 'USD' else btc * float(prices['BTCUSD']['prices'])
                    array[key['currency']] = {
                        'amount': price,
                        'totalbtc': btc,
                        'totalusd': price
                    }

        return array

    def pricesdata(self):
        url = self.baseurl + "2/public/ticker"
        arr = json.loads(requests.get(url).text)
        array = {}
        if 'error' not in array and arr:
            for obj in arr:
                array[obj['symbol']] = {
                    'prices': obj['last'],
                    'bid': obj['bid'],
                    'ask': obj['ask']
                }
        return array

    def _account(self):
        return self._signed_request("2/trading/balance")

    def _signed_request(self, url, parameters=None):
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        body = ''
        if parameters:
            keys = sorted(parameters.keys())
            body = '&'.join(['%s=%s' % (key, urllib.parse.quote(parameters[key], safe='')) for key in keys])

        url = self.baseurl + url + body
        request = self._init_session()
        response = request.get(url).text
        return json.loads(response)
