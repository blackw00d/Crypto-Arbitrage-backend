import base64
import hashlib
import hmac
import datetime
import urllib.parse
import requests
import json


class HuobiAPI:

    def __init__(self, api_key='', api_secret=''):
        self.baseurl = 'api.huobi.pro'
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self):
        session = requests.session()
        session.headers.update(
            {
                'Content-Type': 'application/x-www-form-urlencoded',
                'authType': 'api'
            }
        )
        return session

    def graph(self, quote, base):
        url = 'https://' + self.baseurl + '/market/history/kline?symbol=' \
              + base.lower() + quote.lower() + '&period=1day'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['status'] != 'ok':
            return []
        for tick in ticks['data']:
            x.append({
                'x': tick['id'] * 1000,
                'y': tick['close']
            })
            y.append({
                'x': tick['id'] * 1000,
                'y': tick['vol']
            })
        return [x, y]

    def parsebalance(self):
        arr = self._balance(self._account())
        array = {}
        if 'error' not in arr and arr:
            prices = self.pricesdata()
            for key in arr:
                if float(key['balance']) > 0:
                    btc = float(key['balance']) if key['currency'] == 'btc' \
                        else (float(key['balance']) / float(prices['btcusdt']['prices'])
                              if key['currency'] == 'usdt'
                              else (float(key['balance']) * float(prices[key['currency'] + 'btc']['prices'])
                                    if key['currency'] + 'btc' in prices else 0))
                    price = float(key['balance']) if key['currency'] == 'usdt' \
                        else btc * float(prices['btcusdt']['prices'])
                    array[key['currency'].upper()] = {
                        'amount': float(key['balance']),
                        'totalbtc': btc,
                        'totalusd': price
                    }
        return array

    def pricesdata(self):
        url = 'https://' + self.baseurl + "/market/tickers"
        arr = json.loads(requests.get(url).text)
        array = {}
        if 'status' in arr and arr:
            if arr['status'] == 'ok':
                for obj in arr['data']:
                    array[obj['symbol']] = {
                        'prices': obj['close'],
                        'bid': obj['bid'],
                        'ask': obj['ask']
                    }
        return array

    def _account(self):
        response = self._signed_request("/v1/account/accounts")
        account_id = ''
        if response and 'status' in response:
            if response['status'] == 'ok':
                account_id = str(response['data'][0]['id'])
        return account_id

    def _balance(self, account):
        response = self._signed_request(f"/v1/account/accounts/{account}/balance")
        balance = {}
        if response and 'status' in response:
            if response['status'] == 'ok':
                balance = response['data']['list']
        return balance

    def _signed_request(self, url, method='GET', parameters=None):
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
        header = {
            'AccessKeyId': self.api_key,
            'SignatureMethod': 'HmacSHA256',
            'SignatureVersion': '2',
            'Timestamp': timestamp
        }
        if parameters and len(parameters):
            for key, value in parameters.items():
                header.update({key: value})

        keys = sorted(header.keys())
        body = '&'.join(['%s=%s' % (key, urllib.parse.quote(header[key], safe='')) for key in keys])

        presign = '%s\n%s\n%s\n%s' % (method, self.baseurl, url, body)
        signature_sha256 = hmac.new(self.api_secret.encode('utf-8'), presign.encode('utf-8'), hashlib.sha256).digest()
        signature = base64.b64encode(signature_sha256).decode()
        header.update({'Signature': signature})

        request = self._init_session()
        url = 'https://' + self.baseurl + url + '?' + urllib.parse.urlencode(header)
        response = request.get(url).text
        return json.loads(response)
