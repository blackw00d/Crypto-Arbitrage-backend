import requests
import json


class KucoinAPI:

    def __init__(self):
        self.baseurl = ' https://api.kucoin.com/api/v1/'

    def graph(self, quote, base):
        url = self.baseurl + 'market/candles?type=1day&symbol=' + base + "-" + quote
        print(url)
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['code'] != "200000":
            return []
        for tick in ticks['data']:
            x.append({
                'x': int(tick[0]) * 1000,
                'y': float(tick[2])
            })
            y.append({
                'x': int(tick[0]) * 1000,
                'y': float(tick[6])
            })
        return [x, y]
