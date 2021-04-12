import requests
import json


class KrakenAPI:

    def __init__(self):
        self.baseurl = 'https://api.kraken.com/0/public/'

    def graph(self, quote, base):
        url = self.baseurl + 'OHLC?pair=' + base + quote + '&interval=21600'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['error']:
            return []
        for tick in ticks['result'][base + quote]:
            print(tick)
            x.append({
                'x': tick[0] * 1000,
                'y': float(tick[4])
            })
            y.append({
                'x': tick[0] * 1000,
                'y': float(tick[6])
            })
        return [x, y]
