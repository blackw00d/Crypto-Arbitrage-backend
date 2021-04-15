from django.db import models


class BinanceBittrex(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Bittrex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceHitbtc(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Hitbtc """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceKucoin(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Kucoin """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinancePoloniex(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Poloniex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceKraken(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceOkex(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceGateio(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceBitz(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceBibox(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexHitbtc(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Hitbtc """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexKucoin(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Kucoin """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexPoloniex(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Poloniex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexKraken(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexOkex(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexGateio(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexBitz(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexBibox(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexHitbtc(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Hitbtc """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexKucoin(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Kucoin """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexKraken(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexOkex(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexGateio(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexBitz(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexBibox(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcKucoin(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Kucoin """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class Hitbtckraken(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcOkex(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcGateio(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcBitz(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcBibox(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinKraken(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinOkex(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinGateio(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinBitz(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinBibox(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenOkex(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenGateio(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenBitz(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenBibox(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexGateio(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexBitz(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexBibox(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class GateioBitz(models.Model):
    """ Данные арбитражной торговли между биржами Gateio - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class GateioHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Gateio - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class GateioCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Gateio - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class GateioBibox(models.Model):
    """ Данные арбитражной торговли между биржами Gateio - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BitzHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Bitz - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BitzCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Bitz - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BitzBibox(models.Model):
    """ Данные арбитражной торговли между биржами Bitz - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HuobiCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Huobi - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HuobiBibox(models.Model):
    """ Данные арбитражной торговли между биржами Huobi - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class CoinexBibox(models.Model):
    """ Данные арбитражной торговли между биржами Coinex - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class UserBalance(models.Model):
    """ Данные баланса пользователей """
    user = models.CharField('Имя', max_length=20, default=None, null=True)
    balance = models.TextField('Баланс', default=None, null=True)
    totalbtc = models.FloatField('TotalBTC', default=None, null=True)
    totalusd = models.FloatField('TotalUSD', default=None, null=True)


class CoinListing(models.Model):
    """ Список новых монет, выходящих на биржах """
    exchange = models.CharField('Биржа', max_length=50, default=None, null=True)
    name = models.CharField('Монета', max_length=200, default=None, null=True)
    date = models.DateField('Дата', default=None, null=True)


class ExchangeModel(models.Model):
    """ Базовая модель биржи """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)

    class Meta:
        abstract = True


class Binance(ExchangeModel):
    """ Данные монет на бирже Binance """
    trading = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    deposit = models.CharField('Пополнение', max_length=55, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=55, default=None, null=True)


class Bittrex(ExchangeModel):
    """ Данные монет на бирже Bittrex """
    trading = models.CharField('Объем рынка', max_length=50, default=None, null=True)


class Bibox(ExchangeModel):
    """ Данные монет на бирже Bibox """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)


class Bitz(ExchangeModel):
    """ Данные монет на бирже Bitz """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)


class Gateio(ExchangeModel):
    """ Данные монет на бирже Gateio """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)


class Coinex(ExchangeModel):
    """ Данные монет на бирже Coinex """


class Hitbtc(ExchangeModel):
    """ Данные монет на бирже Hitbtc """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)
    blocks = models.IntegerField('Блоки', default=None, null=True)


class Okex(ExchangeModel):
    """ Данные монет на бирже Okex """


class Huobi(ExchangeModel):
    """ Данные монет на бирже Huobi """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)


class Kraken(ExchangeModel):
    """ Данные монет на бирже Kraken """


class Kucoin(ExchangeModel):
    """ Данные монет на бирже Kucoin """
    trading = models.CharField('Торговля', max_length=50, default=None, null=True)


class Poloniex(ExchangeModel):
    """ Данные монет на бирже Poloniex """
    trading = models.CharField('Торговля', max_length=50, default=None, null=True)
    blocks = models.IntegerField('Блоки', default=None, null=True)


class Trading(models.Model):
    """ Сигналы продажи выбранных пар монет по выбранным показателям дохода """
    user = models.CharField('Имя', max_length=20, default=None, null=True)
    exchange = models.CharField('Биржа', max_length=20, default=None, null=True)
    pair = models.CharField('Пара', max_length=20, default=None, null=True)
    amount = models.FloatField('Количество', default=0, null=True)
    price = models.FloatField('Цена', default=0, null=True)
    stoploss = models.FloatField('StopLoss', default=0, null=True)
    trailingstoploss = models.IntegerField('TrailingStopLoss', default=0, null=True)
    takeprofit = models.FloatField('TakeProfit', default=0, null=True)
    trailingtakeprofit = models.IntegerField('TrailingTakeProfit', default=0, null=True)
    trailingtakeprofitprocent = models.IntegerField('TrailingTakeProfitProcent', default=0, null=True)
    active = models.IntegerField('TrailingTakeProfitProcent', default=0, null=True)
    stoplossvalue = models.FloatField('StopLoss', default=0, null=True)
    stoplosstrailingvalue = models.FloatField('StopLoss', default=0, null=True)
    takeprofitvalue = models.FloatField('StopLoss', default=0, null=True)
    takeprofittrailingvalue = models.FloatField('StopLoss', default=0, null=True)


class Tracking(models.Model):
    """ Отслеживание изменения показателей торговых пар монет на биржах """
    user = models.CharField('Имя', max_length=20, default=None, null=True)
    exchange = models.CharField('Биржа', max_length=20, default=None, null=True)
    pair = models.CharField('Пара', max_length=20, default=None, null=True)
    price = models.FloatField('Цена', default=0, null=False)
    pricechangevalue = models.FloatField('price_change_value', default=0, null=True)
    pricechangeprocent = models.IntegerField('price_change_procent', default=0, null=True)
    priceactive = models.IntegerField('price_active', default=0, null=True)
    volume = models.FloatField('volume', default=0, null=False)
    volumechangevalue = models.FloatField('volume_change_value', default=0, null=True)
    volumechangeprocent = models.IntegerField('volume_change_procent', default=0, null=True)
    volumeactive = models.IntegerField('volume_active', default=0, null=True)


class UserKeys(models.Model):
    """ Секретные ключи пользователей для доступа на биржу """
    user = models.CharField('Имя', max_length=80, default=None, null=True)
    binance_key = models.CharField('Binance Key', max_length=80, default=None, null=True)
    binance_secret = models.CharField('Binance Secret', max_length=80, default=None, null=True)
    bittrex_key = models.CharField('Bittrex Key', max_length=80, default=None, null=True)
    bittrex_secret = models.CharField('Bittrex Secret', max_length=80, default=None, null=True)
    poloniex_key = models.CharField('Poloniex Key', max_length=80, default=None, null=True)
    poloniex_secret = models.CharField('Poloniex Secret', max_length=80, default=None, null=True)
    hitbtc_key = models.CharField('HitBTC Key', max_length=80, default=None, null=True)
    hitbtc_secret = models.CharField('HitBTC Secret', max_length=80, default=None, null=True)
    kucoin_key = models.CharField('Kucoin Key', max_length=80, default=None, null=True)
    kucoin_secret = models.CharField('Kucoin Secret', max_length=80, default=None, null=True)
    kraken_key = models.CharField('Kraken Key', max_length=80, default=None, null=True)
    kraken_secret = models.CharField('Kraken Secret', max_length=80, default=None, null=True)
    huobi_key = models.CharField('Huobi Key', max_length=80, default=None, null=True)
    huobi_secret = models.CharField('Huobi Secret', max_length=80, default=None, null=True)
    okex_key = models.CharField('OKex Key', max_length=80, default=None, null=True)
    okex_secret = models.CharField('OKex Secret', max_length=80, default=None, null=True)
    gateio_key = models.CharField('Gate.io Key', max_length=80, default=None, null=True)
    gateio_secret = models.CharField('Gate.io Secret', max_length=80, default=None, null=True)
    coinex_key = models.CharField('Coinex Key', max_length=80, default=None, null=True)
    coinex_secret = models.CharField('Coinex Secret', max_length=80, default=None, null=True)
    bitz_key = models.CharField('Bit-Z Key', max_length=80, default=None, null=True)
    bitz_secret = models.CharField('Bit-Z Secret', max_length=80, default=None, null=True)
    bibox_key = models.CharField('Bibox Key', max_length=80, default=None, null=True)
    bibox_secret = models.CharField('Bibox Secret', max_length=80, default=None, null=True)
