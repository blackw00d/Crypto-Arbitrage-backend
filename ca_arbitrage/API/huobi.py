import requests
import json


class HuobiAPI:

    def __init__(self):
        self.baseurl = 'https://api.huobi.pro/market/'

    def graph(self, quote, base):
        url = self.baseurl + 'history/kline?symbol=' + base.lower() + quote.lower()+ '&period=1day'
        ticks = json.loads(requests.get(url).text)
        x = []
        y = []
        if ticks['status'] != 'ok':
            return []
        for tick in ticks['data']:
            x.append({
                'x': tick['id'] * 1000,
                'y': tick['close']
            })
            y.append({
                'x': tick['id'] * 1000,
                'y': tick['vol']
            })
        return [x, y]
