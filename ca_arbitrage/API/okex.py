import requests
import json


class OKexAPI:

    def __init__(self):
        self.baseurl = 'https://www.okex.com/api/v5/'

    def graph(self, quote, base):
        url = self.baseurl + 'market/candles?instId=' + base + "-" + quote + '&bar=1D'
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
