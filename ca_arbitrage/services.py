import pandas as pd

from ca_arbitrage.serializers import *
from .API.bibox import BiboxAPI
from .API.binance import BinanceAPI
from .API.bittrex import BittrexAPI
from .API.bitz import BitZAPI
from .API.coinex import CoinexAPI
from .API.gateio import GateIOAPI
from .API.hitbtc import HitBTCAPI
from .API.huobi import HuobiAPI
from .API.kraken import KrakenAPI
from .API.kucoin import KucoinAPI
from .API.okex import OKexAPI
from .API.poloniex import PoloniexAPI
from rest_framework import status
import pandas


def get_user_balance(user):
    """ ПОЛУЧЕНИЕ БАЛАНСА ПОЛЬЗОВАТЕЛЯ """
    balance = UsersBalance.objects.get(user__username=user)
    serializer = BalanceSerializer(balance)
    return serializer.data


def get_coin_listing():
    """ ПОЛУЧЕНИЕ СПИСКА ДОБАВЛЕННЫХ НА БИРЖИ МОНЕТ """
    listing = CoinListing.objects.all().order_by('date')
    serializer = CoinListingSerializer(listing, many=True)
    return serializer.data


def get_exchange_data():
    """ ПОЛУЧЕНИЕ ДАННЫХ СО ВСЕХ БИРЖ """
    filters = {
        'binance': Binance.objects.all().order_by('name'),
        'bittrex': Bittrex.objects.all().order_by('name'),
        'poloniex': Poloniex.objects.all().order_by('name'),
        'hitbtc': Hitbtc.objects.all().order_by('name'),
        'kucoin': Kucoin.objects.all().order_by('name'),
        'kraken': Kraken.objects.all().order_by('name'),
        'huobi': Huobi.objects.all().order_by('name'),
        'okex': Okex.objects.all().order_by('name'),
        'gateio': Gateio.objects.all().order_by('name'),
        'coinex': Coinex.objects.all().order_by('name'),
        'bitz': Bitz.objects.all().order_by('name'),
        'bibox': Bibox.objects.all().order_by('name')
    }
    serializer = ExchangesSerializers(filters)
    return serializer.data


def get_graph_data(exchange, coin):
    """ ПОЛУЧЕНИЕ ГРАФИКА ЦЕНЫ И ОБЪЕМА МОНЕТЫ """
    exchanges_list = {
        'binance': {'api': BinanceAPI()},
        'bittrex': {'api': BittrexAPI()},
        'poloniex': {'api': PoloniexAPI()},
        'hitbtc': {'api': HitBTCAPI()},
        'kucoin': {'api': KucoinAPI()},
        'kraken': {'api': KrakenAPI()},
        'huobi': {'api': HuobiAPI()},
        'okex': {'api': OKexAPI()},
        'gateio': {'api': GateIOAPI()},
        'coinex': {'api': CoinexAPI()},
        'bitz': {'api': BitZAPI()},
        'bibox': {'api': BiboxAPI()}
    }

    if exchange in exchanges_list:
        api = exchanges_list[exchange]['api']
        quote, base = coin['coin'].split('-')
        x_y = api.graph(quote, base)
        candles = pd.DataFrame().from_dict(x_y[0])

        sma10 = []
        sma10_dataframe = candles.rolling(window=10).mean().dropna()
        if not sma10_dataframe.empty:
            sma10 = sma10_dataframe.to_dict('records')
        x_y.append(sma10)

        sma30 = []
        sma30_dataframe = candles.rolling(window=30).mean().dropna()
        if not sma30_dataframe.empty:
            sma30 = sma30_dataframe.to_dict('records')
        x_y.append(sma30)

        return x_y, status.HTTP_200_OK
    else:
        return [], status.HTTP_400_BAD_REQUEST


def sort_arbitrage_data(data):
    """ ПРЕОБРАЗОВАНИЕ ДАННЫХ АРБИТРАЖА НА МАССИВЫ ДАННЫХ ПО ПРОФИТУ И МОНЕТАМ """
    temp = {}
    profit_array = []
    coin_array = []

    for (key, values) in data.items():
        exchange = key.split('_')
        for value in values:
            name = value['name'].split('-')[1]
            coin_array.append({
                'name': name,
                'price_a': value['price_a'],
                'price_b': value['price_b'],
                'profit': value['profit'],
                'link_a': value['link_a'],
                'link_b': value['link_b'],
                'exchange_a': exchange[0],
                'exchange_b': exchange[1],
                'index': 0,
                'amount': 1
            })
            if name in temp:
                if temp[name]['profit'] < value['profit']:
                    temp[name] = {
                        'price_a': value['price_a'],
                        'price_b': value['price_b'],
                        'profit': value['profit'],
                        'link_a': value['link_a'],
                        'link_b': value['link_b'],
                        'exchange_a': exchange[0],
                        'exchange_b': exchange[1]
                    }
            else:
                temp[name] = {
                    'price_a': value['price_a'],
                    'price_b': value['price_b'],
                    'profit': value['profit'],
                    'link_a': value['link_a'],
                    'link_b': value['link_b'],
                    'exchange_a': exchange[0],
                    'exchange_b': exchange[1]
                }

    sorted_coin_array = sorted(coin_array, key=lambda v: (v['name'], -v['profit']))

    temp = dict(sorted(temp.items(), key=lambda v: -v[1]['profit']))
    for key in temp:
        profit_array.append({
            'name': key,
            'price_a': temp[key]['price_a'],
            'price_b': temp[key]['price_b'],
            'profit': temp[key]['profit'],
            'link_a': temp[key]['link_a'],
            'link_b': temp[key]['link_b'],
            'exchange_a': temp[key]['exchange_a'],
            'exchange_b': temp[key]['exchange_b']
        })

    return [profit_array, sorted_coin_array]


def get_arbitrage_data():
    """ ПОЛУЧЕНИЕ ДАННЫХ АРБИТРАЖА НА БИРЖАХ """
    filters = {}
    min_volume = 30000
    min_profit = 0.01
    max_profit = 100
    filters['binance_bittrex'] = BinanceBittrex.objects.filter(binance_volume__gt=min_volume,
                                                               bittrex_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['binance_hitbtc'] = BinanceHitbtc.objects.filter(binance_volume__gt=min_volume,
                                                             hitbtc_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['binance_kucoin'] = BinanceKucoin.objects.filter(binance_volume__gt=min_volume,
                                                             kucoin_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['binance_poloniex'] = BinancePoloniex.objects.filter(binance_volume__gt=min_volume,
                                                                 poloniex_volume__gt=min_volume,
                                                                 profit__gt=min_profit,
                                                                 profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['binance_kraken'] = BinanceKraken.objects.filter(binance_volume__gt=min_volume,
                                                             kraken_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['binance_okex'] = BinanceOkex.objects.filter(binance_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['binance_gateio'] = BinanceGateio.objects.filter(binance_volume__gt=min_volume,
                                                             gateio_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['binance_bitz'] = BinanceBitz.objects.filter(binance_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['binance_huobi'] = BinanceHuobi.objects.filter(binance_volume__gt=min_volume,
                                                           huobi_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['binance_coinex'] = BinanceCoinex.objects.filter(binance_volume__gt=min_volume,
                                                             coinex_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['binance_bibox'] = BinanceBibox.objects.filter(binance_volume__gt=min_volume,
                                                           bibox_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['bittrex_hitbtc'] = BittrexHitbtc.objects.filter(bittrex_volume__gt=min_volume,
                                                             hitbtc_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['bittrex_kucoin'] = BittrexKucoin.objects.filter(bittrex_volume__gt=min_volume,
                                                             kucoin_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['bittrex_poloniex'] = BittrexPoloniex.objects.filter(bittrex_volume__gt=min_volume,
                                                                 poloniex_volume__gt=min_volume,
                                                                 profit__gt=min_profit,
                                                                 profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['bittrex_kraken'] = BittrexKraken.objects.filter(bittrex_volume__gt=min_volume,
                                                             kraken_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['bittrex_okex'] = BittrexOkex.objects.filter(bittrex_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['bittrex_gateio'] = BittrexGateio.objects.filter(bittrex_volume__gt=min_volume,
                                                             gateio_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['bittrex_bitz'] = BittrexBitz.objects.filter(bittrex_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['bittrex_huobi'] = BittrexHuobi.objects.filter(bittrex_volume__gt=min_volume,
                                                           huobi_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['bittrex_coinex'] = BittrexCoinex.objects.filter(bittrex_volume__gt=min_volume,
                                                             coinex_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['bittrex_bibox'] = BittrexBibox.objects.filter(bittrex_volume__gt=min_volume,
                                                           bibox_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['poloniex_hitbtc'] = PoloniexHitbtc.objects.filter(poloniex_volume__gt=min_volume,
                                                               hitbtc_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['poloniex_kucoin'] = PoloniexKucoin.objects.filter(poloniex_volume__gt=min_volume,
                                                               kucoin_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['poloniex_kraken'] = PoloniexKraken.objects.filter(poloniex_volume__gt=min_volume,
                                                               kraken_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['poloniex_okex'] = PoloniexOkex.objects.filter(poloniex_volume__gt=min_volume,
                                                           okex_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['poloniex_gateio'] = PoloniexGateio.objects.filter(poloniex_volume__gt=min_volume,
                                                               gateio_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['poloniex_bitz'] = PoloniexBitz.objects.filter(poloniex_volume__gt=min_volume,
                                                           bitz_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['poloniex_huobi'] = PoloniexHuobi.objects.filter(poloniex_volume__gt=min_volume,
                                                             huobi_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['poloniex_coinex'] = PoloniexCoinex.objects.filter(poloniex_volume__gt=min_volume,
                                                               coinex_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['poloniex_bibox'] = PoloniexBibox.objects.filter(poloniex_volume__gt=min_volume,
                                                             bibox_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['hitbtc_kucoin'] = HitbtcKucoin.objects.filter(hitbtc_volume__gt=min_volume,
                                                           kucoin_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_kraken'] = Hitbtckraken.objects.filter(hitbtc_volume__gt=min_volume,
                                                           kraken_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_okex'] = HitbtcOkex.objects.filter(hitbtc_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_gateio'] = HitbtcGateio.objects.filter(hitbtc_volume__gt=min_volume,
                                                           gateio_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_bitz'] = HitbtcBitz.objects.filter(hitbtc_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_huobi'] = HitbtcHuobi.objects.filter(hitbtc_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_coinex'] = HitbtcCoinex.objects.filter(hitbtc_volume__gt=min_volume,
                                                           coinex_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_bibox'] = HitbtcBibox.objects.filter(hitbtc_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_kraken'] = KucoinKraken.objects.filter(kucoin_volume__gt=min_volume,
                                                           kraken_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_okex'] = KucoinOkex.objects.filter(kucoin_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_gateio'] = KucoinGateio.objects.filter(kucoin_volume__gt=min_volume,
                                                           gateio_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_bitz'] = KucoinBitz.objects.filter(kucoin_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_huobi'] = KucoinHuobi.objects.filter(kucoin_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_coinex'] = KucoinCoinex.objects.filter(kucoin_volume__gt=min_volume,
                                                           coinex_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_bibox'] = KucoinBibox.objects.filter(kucoin_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_okex'] = KrakenOkex.objects.filter(kraken_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_gateio'] = KrakenGateio.objects.filter(kraken_volume__gt=min_volume,
                                                           gateio_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_bitz'] = KrakenBitz.objects.filter(kraken_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_huobi'] = KrakenHuobi.objects.filter(kraken_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_coinex'] = KrakenCoinex.objects.filter(kraken_volume__gt=min_volume,
                                                           coinex_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_bibox'] = KrakenBibox.objects.filter(kraken_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['okex_gateio'] = OkexGateio.objects.filter(okex_volume__gt=min_volume, gateio_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['okex_bitz'] = OkexBitz.objects.filter(okex_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                   profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['okex_huobi'] = OkexHuobi.objects.filter(okex_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                     profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['okex_coinex'] = OkexCoinex.objects.filter(okex_volume__gt=min_volume, coinex_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['okex_bibox'] = OkexBibox.objects.filter(okex_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                     profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['gateio_bitz'] = GateioBitz.objects.filter(gateio_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['gateio_huobi'] = GateioHuobi.objects.filter(gateio_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['gateio_coinex'] = GateioCoinex.objects.filter(gateio_volume__gt=min_volume,
                                                           coinex_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['gateio_bibox'] = GateioBibox.objects.filter(gateio_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['bitz_huobi'] = BitzHuobi.objects.filter(bitz_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                     profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['bitz_coinex'] = BitzCoinex.objects.filter(bitz_volume__gt=min_volume, coinex_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['bitz_bibox'] = BitzBibox.objects.filter(bitz_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                     profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['huobi_coinex'] = HuobiCoinex.objects.filter(huobi_volume__gt=min_volume, coinex_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['huobi_bibox'] = HuobiBibox.objects.filter(huobi_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['coinex_bibox'] = CoinexBibox.objects.filter(coinex_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    serializer = ArbitrageSerializers(filters)
    table = serializer.data
    coin_profit = sort_arbitrage_data(table)
    return [table, coin_profit[0], coin_profit[1]]


def get_trading_coins(user):
    """ ПОЛУЧЕНИЕ СПИСКА ТОРГУЕМЫХ МОНЕТ ДЛЯ ПОЛЬЗОВАТЕЛЯ """
    trading = Trading.objects.filter(user__username=user)
    serializer = TradingSerializer(trading, many=True)
    return serializer.data


def get_tracking_coins(user):
    """ ПОЛУЧЕНИЕ СПИСКА ОТСЛЕЖИВАЕМЫХ МОНЕТ ДЛЯ ПОЛЬЗОВАТЕЛЯ """
    tracking = Tracking.objects.filter(user__username=user)
    serializer = TrackingSerializer(tracking, many=True)
    return serializer.data


def get_user_keys(user):
    """ ПОЛУЧЕНИЕ СПИСКА КЛЮЧЕЙ ДЛЯ ПОЛЬЗОВАТЕЛЯ """
    keys = UsersKeys.objects.get(user__username=user)
    serializer = UserKeysSerializer(keys)
    return serializer.data


def get_user_account(user):
    """ ПОЛУЧЕНИЕ СПИСКА КЛЮЧЕЙ ДЛЯ ПОЛЬЗОВАТЕЛЯ """
    account = UsersAccount.objects.get(user__username=user)
    serializer = UsersAccountSerializer(account)
    return serializer.data


def get_user_payments(user):
    """ ПОЛУЧЕНИЕ СПИСКА КЛЮЧЕЙ ДЛЯ ПОЛЬЗОВАТЕЛЯ """
    payments = UsersPayments.objects.filter(user__username=user).order_by('-pay_time', '-id')
    if not payments:
        return []
    serializer = UsersPaymentsSerializer(payments, many=True)
    return serializer.data


def days_value(money):
    """ РАСЧЕТ КОЛИЧЕСТВА ОПЛАЧЕННЫХ ДНЕЙ ПО СУММЕ ПЛАТЕЖА """
    if money == settings.PAYMENT:
        return 30
    elif money == settings.PAYMENT * 2.75:
        return 3 * 30
    elif money == settings.PAYMENT * 5:
        return 6 * 30
    return money / settings.PAYMENT * 30


def set_user_account(data):
    """ ОБНОВЛЕНИЕ ДАННЫХ АККАУНТА ПОЛЬЗОВАТЕЛЯ """
    queryset = UsersAccount.objects.get(user=data['user'])
    days_to_deadline = UsersAccountSerializer(queryset).data['days_to_deadline']
    days = {'days': days_to_deadline + days_value(int(data['money']))}
    serializer = UsersAccountSerializer(queryset, data=days, partial=True)
    if serializer.is_valid():
        serializer.save()
