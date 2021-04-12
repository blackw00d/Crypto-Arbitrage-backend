import requests
import json


class PoloniexAPI:

    def __init__(self):
        self.baseurl = 'https://poloniex.com/public'

    def graph(self, quote, base):
        url = self.baseurl + '?command=returnChartData&currencyPair=' + quote + "_" + base + \
              '&start=1325376000&end=9999999999&period=86400'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if 'error' in ticks:
            return []
        for tick in ticks:
            x.append({
                'x': tick['date'] * 1000,
                'y': tick['close']
            })
            y.append({
                'x': tick['date'] * 1000,
                'y': tick['quoteVolume']
            })
        return [x, y]
