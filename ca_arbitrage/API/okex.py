import base64
import datetime
import hashlib
import hmac
import urllib.parse
import requests
import json


class OKexAPI:

    def __init__(self, api_key='', api_secret='', password=''):
        self.baseurl = 'https://www.okex.com'
        self.api_key = api_key
        self.api_secret = api_secret
        self.password = password

    def _init_session(self, timestamp, signature):
        session = requests.session()
        session.headers.update(
            {
                'OK-ACCESS-KEY': self.api_key,
                'OK-ACCESS-SIGN': signature,
                'OK-ACCESS-TIMESTAMP': timestamp,
                'OK-ACCESS-PASSPHRASE': self.password
            }
        )
        return session

    def graph(self, quote, base):
        url = self.baseurl + '/api/v5/market/candles?instId=' + base + "-" + quote + '&bar=1D'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['code'] != '0':
            return []
        for tick in ticks['data']:
            x.append({
                'x': int(tick[0]),
                'y': float(tick[4])
            })
            y.append({
                'x': int(tick[0]),
                'y': float(tick[6])
            })
        return [x, y]

    def parsebalance(self):
        arr = self._account()
        array = {}

        if arr and 'code' in arr:
            if arr['code'] == '0':
                prices = self.pricesdata()
                for key in arr:
                    if float(key['balance']) > 0:
                        btc = float(key['balance']) if key['currency'] == 'BTC' \
                            else (float(key['balance']) / float(prices['BTC-USDT']['prices'])
                                  if key['currency'] == 'USDT'
                                  else (float(key['balance']) * float(prices[key['currency'] + '-BTC']['prices'])
                                        if key['currency'] + '-BTC' in prices else 0))
                        price = float(key['balance']) if key['currency'] == 'USDT' \
                            else btc * float(prices['BTC-USDT']['prices'])
                        array[key['currency']] = {
                            'amount': float(key['balance']),
                            'totalbtc': btc,
                            'totalusd': price
                        }

        return array

    def pricesdata(self):
        url = self.baseurl + "/api/v5/market/tickers?instType=SPOT"
        arr = json.loads(requests.get(url).text)
        array = {}

        if arr and 'code' in arr:
            if arr['code'] == 0:
                for obj in arr['data']:
                    array[obj['instId']] = {
                        'prices': obj['last'],
                        'bid': obj['bidPx'],
                        'ask': obj['askPx']
                    }
        return array

    def _account(self):
        return self._signed_request("/api/account/v3/wallet")

    def _signed_request(self, url, method='GET', parameters=None):
        if parameters is None:
            parameters = {}
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        timestamp = datetime.datetime.utcnow().isoformat("T", "milliseconds") + 'Z'
        body = ''
        if parameters and len(parameters):
            if method == 'GET':
                url += '?' + '&'.join(['%s=%s' % (key, urllib.parse.quote(parameters[key], safe=''))
                                       for key in parameters.keys()])
            else:
                body = json.dumps(parameters)

        presign = ''.join([timestamp, method, url, body])
        signature_sha256 = hmac.new(self.api_secret.encode('utf-8'), presign.encode('utf-8'), hashlib.sha256).digest()
        signature = base64.b64encode(signature_sha256).decode()

        request = self._init_session(timestamp, signature)
        if method == 'GET':
            response = request.get(self.baseurl + url).text
        elif method == 'POST':
            response = request.post(self.baseurl + url, body)
        elif method == 'DELETE':
            response = request.delete(self.baseurl + url)
        return json.loads(response)
