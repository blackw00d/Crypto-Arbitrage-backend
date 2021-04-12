from datetime import datetime
import requests
import json


class HitBTCAPI:

    def __init__(self):
        self.baseurl = 'https://api.hitbtc.com/api/2/public/'

    def graph(self, quote, base):
        url = self.baseurl + 'candles/' + base + quote + '?period=Ds1'
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
