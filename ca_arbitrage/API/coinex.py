import requests
import json


class CoinexAPI:

    def __init__(self):
        self.baseurl = 'https://api.coinex.com/v1/market/'

    def graph(self, quote, base):
        url = self.baseurl + 'kline?market=' + base + quote + '&type=1day'
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
