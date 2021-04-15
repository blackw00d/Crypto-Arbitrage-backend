import requests
import json


class BinanceAPI:

    def __init__(self):
        self.baseurl = 'https://api.binance.com/api/'

    def graph(self, quote, base):
        ticks = self.request("v3/klines", {'symbol': base + quote, 'interval': '1d'})
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

    def request(self, func, parameters=None):
        url = self.baseurl + func
        if parameters:
            url += '?'
            for k, v in parameters.items():
                url += str(k) + '=' + str(v) + '&'
            url = url[:-1]
        return json.loads(requests.get(url).text)
