import requests
import json


class BitZAPI:

    def __init__(self):
        self.baseurl = 'https://apiv2.bitz.com/Market/'

    def graph(self, quote, base):
        url = self.baseurl + 'kline?symbol=' + base.lower() + '_' + quote.lower() + '&resolution=1day'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['status'] != 200:
            return []
        for tick in ticks['data']['bars']:
            x.append({
                'x': int(tick['time']),
                'y': float(tick['close'])
            })
            y.append({
                'x': int(tick['time']),
                'y': float(tick['volume'])
            })
        return [x, y]
