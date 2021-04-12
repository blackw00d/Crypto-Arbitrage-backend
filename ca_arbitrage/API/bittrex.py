from datetime import datetime
import requests
import json


class BittrexAPI:

    def __init__(self):
        self.baseurl = 'https://api.bittrex.com/'

    def graph(self, quote, base):
        url = self.baseurl + "v3/markets/" + base + "-" + quote + "/candles/TRADE/DAY_1/recent"
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if 'code' in ticks:
            return []
        for tick in ticks:
            x.append({
                'x': int(datetime.strptime(tick['startsAt'], '%Y-%m-%dT%H:%M:%SZ').timestamp() * 1000),
                'y': float(tick['close'])
            })
            y.append({
                'x': int(datetime.strptime(tick['startsAt'], '%Y-%m-%dT%H:%M:%SZ').timestamp() * 1000),
                'y': float(tick['quoteVolume'])
            })
        return [x, y]
