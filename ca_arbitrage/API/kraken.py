import base64
import hashlib
import hmac
import time
import urllib.parse
import requests
import json


class KrakenAPI:

    def __init__(self, api_key='', api_secret=''):
        self.baseurl = 'https://api.kraken.com'
        self.api_key = api_key
        self.api_secret = api_secret

    def _init_session(self, signature):
        session = requests.session()
        session.headers.update(
            {
                "API-Key": self.api_key,
                "API-Sign": signature,
            }
        )
        return session

    def graph(self, quote, base):
        base = base.replace('BTC', 'XBT')
        quote = quote.replace('BTC', 'XBT')
        url = self.baseurl + '/0/public/OHLC?pair=' + base + quote + '&interval=21600'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['error']:
            return []
        for tick in ticks['result'][base.replace('XBT', 'XXBTZ') + quote]:
            x.append({
                'x': tick[0] * 1000,
                'y': float(tick[4])
            })
            y.append({
                'x': tick[0] * 1000,
                'y': float(tick[6])
            })
        return [x, y]

    def _account(self):
        """ НЕ РАБОТАЕТ :( """
        return self._signed_request("/0/private/Balance")

    def _signed_request(self, url, parameters=None):
        if parameters is None:
            parameters = {}
        if self.api_key == '':
            return "signedRequest error: API Key not set!"
        if self.api_secret == '':
            return "signedRequest error: API Secret not set!"

        parameters['nonce'] = int(time.time() * 1000)
        body = (str(parameters['nonce']) + urllib.parse.urlencode(parameters)).encode()
        presign = url.encode() + hashlib.sha256(body).digest()

        signature_sha512 = hmac.new(base64.b64decode(self.api_secret), presign, hashlib.sha512).digest()
        signature = base64.b64encode(signature_sha512).decode()

        request = self._init_session(signature)
        response = request.post(self.baseurl + url, data=parameters).text
        return json.loads(response)
