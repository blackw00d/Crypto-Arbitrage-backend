import requests
import json


class BiboxAPI:

    def __init__(self):
        self.baseurl = 'https://api.bibox.com/v3/mdata/'

    def graph(self, quote, base):
        url = self.baseurl + 'kline?pair=' + base + "_" + quote + '&period=day'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['state'] != 0:
            return []
        for tick in ticks['result']:
            x.append({
                'x': tick['time'],
                'y': float(tick['close'])
            })
            y.append({
                'x': tick['time'],
                'y': float(tick['vol'])
            })
        return [x, y]
