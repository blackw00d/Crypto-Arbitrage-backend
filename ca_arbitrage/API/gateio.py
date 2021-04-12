import requests
import json


class GataIOAPI:

    def __init__(self):
        self.baseurl = 'https://api.gateio.ws/api/v4/spot/'

    def graph(self, quote, base):
        url = self.baseurl + 'candlesticks?currency_pair=' + base + "_" + quote + '&interval=1d'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if 'label' in ticks:
            return []
        for tick in ticks:
            x.append({
                'x': int(tick[0]) * 1000,
                'y': float(tick[2])
            })
            y.append({
                'x': int(tick[0]) * 1000,
                'y': float(tick[1])
            })
        return [x, y]
