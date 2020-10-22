from ca_arbitrage.serializers import *


def get_user_balance(user):
    """ Вывод баланса пользователя """
    balance = UserBalance.objects.get(user=user)
    serializer = BalanceSerializer(balance)
    return serializer.data


def get_coin_listing():
    """ Вывод списка появившихся монет """
    listing = CoinListing.objects.all().order_by('date')
    serializer = CoinListingSerializer(listing, many=True)
    return serializer.data


def get_exchange_data():
    """ Получение данных с бирж """
    filters = {}
    filters['binance'] = Binance.objects.all().order_by('name')
    filters['bittrex'] = Bittrex.objects.all().order_by('name')
    filters['poloniex'] = Poloniex.objects.all().order_by('name')
    filters['hitbtc'] = Hitbtc.objects.all().order_by('name')
    filters['livecoin'] = Livecoin.objects.all().order_by('name')
    filters['kucoin'] = Kucoin.objects.all().order_by('name')
    filters['kraken'] = Kraken.objects.all().order_by('name')
    filters['huobi'] = Huobi.objects.all().order_by('name')
    filters['okex'] = Okex.objects.all().order_by('name')
    filters['gateio'] = Gateio.objects.all().order_by('name')
    filters['coinex'] = Coinex.objects.all().order_by('name')
    filters['bitz'] = Bitz.objects.all().order_by('name')
    filters['bibox'] = Bibox.objects.all().order_by('name')
    serializer = ExchangesSerializers(filters)
    return serializer.data


def get_arbitrage_data():
    """ Получение арбитражных данных о биржах """
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
    filters['binance_livecoin'] = BinanceLivecoin.objects.filter(binance_volume__gt=min_volume,
                                                                 livecoin_volume__gt=min_volume,
                                                                 profit__gt=min_profit,
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
    filters['binance_huobi'] = BinanceHuobi.objects.filter(binance_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['binance_coinex'] = BinanceCoinex.objects.filter(binance_volume__gt=min_volume,
                                                             coinex_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['binance_bibox'] = BinanceBibox.objects.filter(binance_volume__gt=min_volume, bibox_volume__gt=min_volume,
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
    filters['bittrex_livecoin'] = BittrexLivecoin.objects.filter(bittrex_volume__gt=min_volume,
                                                                 livecoin_volume__gt=min_volume,
                                                                 profit__gt=min_profit,
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
    filters['bittrex_huobi'] = BittrexHuobi.objects.filter(bittrex_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['bittrex_coinex'] = BittrexCoinex.objects.filter(bittrex_volume__gt=min_volume,
                                                             coinex_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['bittrex_bibox'] = BittrexBibox.objects.filter(bittrex_volume__gt=min_volume, bibox_volume__gt=min_volume,
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
    filters['poloniex_livecoin'] = PoloniexLivecoin.objects.filter(poloniex_volume__gt=min_volume,
                                                                   livecoin_volume__gt=min_volume,
                                                                   profit__gt=min_profit,
                                                                   profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['poloniex_kraken'] = PoloniexKraken.objects.filter(poloniex_volume__gt=min_volume,
                                                               kraken_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['poloniex_okex'] = PoloniexOkex.objects.filter(poloniex_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['poloniex_gateio'] = PoloniexGateio.objects.filter(poloniex_volume__gt=min_volume,
                                                               gateio_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['poloniex_bitz'] = PoloniexBitz.objects.filter(poloniex_volume__gt=min_volume, bitz_volume__gt=min_volume,
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
    filters['hitbtc_kucoin'] = HitbtcKucoin.objects.filter(hitbtc_volume__gt=min_volume, kucoin_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_livecoin'] = HitbtcLivecoin.objects.filter(hitbtc_volume__gt=min_volume,
                                                               livecoin_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['hitbtc_kraken'] = Hitbtckraken.objects.filter(hitbtc_volume__gt=min_volume, kraken_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_okex'] = HitbtcOkex.objects.filter(hitbtc_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_gateio'] = HitbtcGateio.objects.filter(hitbtc_volume__gt=min_volume, gateio_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_bitz'] = HitbtcBitz.objects.filter(hitbtc_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_huobi'] = HitbtcHuobi.objects.filter(hitbtc_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_coinex'] = HitbtcCoinex.objects.filter(hitbtc_volume__gt=min_volume, coinex_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['hitbtc_bibox'] = HitbtcBibox.objects.filter(hitbtc_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_livecoin'] = KucoinLivecoin.objects.filter(kucoin_volume__gt=min_volume,
                                                               livecoin_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['kucoin_kraken'] = KucoinKraken.objects.filter(kucoin_volume__gt=min_volume, kraken_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_okex'] = KucoinOkex.objects.filter(kucoin_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_gateio'] = KucoinGateio.objects.filter(kucoin_volume__gt=min_volume, gateio_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_bitz'] = KucoinBitz.objects.filter(kucoin_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_huobi'] = KucoinHuobi.objects.filter(kucoin_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_coinex'] = KucoinCoinex.objects.filter(kucoin_volume__gt=min_volume, coinex_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kucoin_bibox'] = KucoinBibox.objects.filter(kucoin_volume__gt=min_volume, bibox_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['livecoin_kraken'] = LivecoinKraken.objects.filter(livecoin_volume__gt=min_volume,
                                                               kraken_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['livecoin_okex'] = LivecoinOkex.objects.filter(livecoin_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['livecoin_gateio'] = LivecoinGateio.objects.filter(livecoin_volume__gt=min_volume,
                                                               gateio_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['livecoin_bitz'] = LivecoinBitz.objects.filter(livecoin_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['livecoin_huobi'] = LivecoinHuobi.objects.filter(livecoin_volume__gt=min_volume,
                                                             huobi_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['livecoin_coinex'] = LivecoinCoinex.objects.filter(livecoin_volume__gt=min_volume,
                                                               coinex_volume__gt=min_volume, profit__gt=min_profit,
                                                               profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['livecoin_bibox'] = LivecoinBibox.objects.filter(livecoin_volume__gt=min_volume,
                                                             bibox_volume__gt=min_volume, profit__gt=min_profit,
                                                             profit__lt=max_profit).order_by('name').order_by(
        '-profit')
    filters['kraken_okex'] = KrakenOkex.objects.filter(kraken_volume__gt=min_volume, okex_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_gateio'] = KrakenGateio.objects.filter(kraken_volume__gt=min_volume, gateio_volume__gt=min_volume,
                                                           profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_bitz'] = KrakenBitz.objects.filter(kraken_volume__gt=min_volume, bitz_volume__gt=min_volume,
                                                       profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_huobi'] = KrakenHuobi.objects.filter(kraken_volume__gt=min_volume, huobi_volume__gt=min_volume,
                                                         profit__gt=min_profit, profit__lt=max_profit).order_by(
        'name').order_by('-profit')
    filters['kraken_coinex'] = KrakenCoinex.objects.filter(kraken_volume__gt=min_volume, coinex_volume__gt=min_volume,
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
    filters['gateio_coinex'] = GateioCoinex.objects.filter(gateio_volume__gt=min_volume, coinex_volume__gt=min_volume,
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
    return serializer.data


def get_trading_coins(user):
    """ Получение списка торгуемых монет для пользователя """
    trading = Trading.objects.filter(user=user)
    serializer = TradingSerializer(trading, many=True)
    return serializer.data


def get_tracking_coins(user):
    """ Получение списка отслеживаемых монет для пользователя """
    tracking = Tracking.objects.filter(user=user)
    serializer = TrackingSerializer(tracking, many=True)
    return serializer.data
