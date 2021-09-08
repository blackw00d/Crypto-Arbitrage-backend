from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib import admin


class BinanceBittrex(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Bittrex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_bittrex'


class BinanceHitbtc(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Hitbtc """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_hitbtc'


class BinanceKucoin(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Kucoin """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_kucoin'


class BinancePoloniex(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Poloniex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_poloniex'


class BinanceKraken(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_kraken'


class BinanceOkex(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_okex'


class BinanceGateio(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_gateio'


class BinanceBitz(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_bitz'


class BinanceHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_huobi'


class BinanceCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_coinex'


class BinanceBibox(models.Model):
    """ Данные арбитражной торговли между биржами Binance - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'binance_bibox'


class BittrexHitbtc(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Hitbtc """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_hitbtc'


class BittrexKucoin(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Kucoin """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_kucoin'


class BittrexPoloniex(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Poloniex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_poloniex'


class BittrexKraken(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_kraken'


class BittrexOkex(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_okex'


class BittrexGateio(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_gateio'


class BittrexBitz(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_bitz'


class BittrexHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_huobi'


class BittrexCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_coinex'


class BittrexBibox(models.Model):
    """ Данные арбитражной торговли между биржами Bittrex - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bittrex_bibox'


class PoloniexHitbtc(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Hitbtc """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'poloniex_hitbtc'


class PoloniexKucoin(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Kucoin """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'poloniex_kucoin'


class PoloniexKraken(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'poloniex_kraken'


class PoloniexOkex(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'poloniex_okex'


class PoloniexGateio(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'poloniex_gateio'


class PoloniexBitz(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'poloniex_bitz'


class PoloniexHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'poloniex_huobi'


class PoloniexCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'poloniex_coinex'


class PoloniexBibox(models.Model):
    """ Данные арбитражной торговли между биржами Poloniex - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'poloniex_bibox'


class HitbtcKucoin(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Kucoin """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'hitbtc_kucoin'


class Hitbtckraken(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'hitbtc_kraken'


class HitbtcOkex(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'hitbtc_okex'


class HitbtcGateio(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'hitbtc_gateio'


class HitbtcBitz(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'hitbtc_bitz'


class HitbtcHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'hitbtc_huobi'


class HitbtcCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'hitbtc_coinex'


class HitbtcBibox(models.Model):
    """ Данные арбитражной торговли между биржами Hitbtc - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'hitbtc_bibox'


class KucoinKraken(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Kraken """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kucoin_kraken'


class KucoinOkex(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kucoin_okex'


class KucoinGateio(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kucoin_gateio'


class KucoinBitz(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kucoin_bitz'


class KucoinHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kucoin_huobi'


class KucoinCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kucoin_coinex'


class KucoinBibox(models.Model):
    """ Данные арбитражной торговли между биржами Kucoin - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kucoin_bibox'


class KrakenOkex(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Okex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kraken_okex'


class KrakenGateio(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kraken_gateio'


class KrakenBitz(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kraken_bitz'


class KrakenHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kraken_huobi'


class KrakenCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kraken_coinex'


class KrakenBibox(models.Model):
    """ Данные арбитражной торговли между биржами Kraken - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'kraken_bibox'


class OkexGateio(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Gateio """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'okex_gateio'


class OkexBitz(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'okex_bitz'


class OkexHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'okex_huobi'


class OkexCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'okex_coinex'


class OkexBibox(models.Model):
    """ Данные арбитражной торговли между биржами Okex - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'okex_bibox'


class GateioBitz(models.Model):
    """ Данные арбитражной торговли между биржами Gateio - Bitz """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'gateio_bitz'


class GateioHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Gateio - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'gateio_huobi'


class GateioCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Gateio - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'gateio_coinex'


class GateioBibox(models.Model):
    """ Данные арбитражной торговли между биржами Gateio - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'gateio_bibox'


class BitzHuobi(models.Model):
    """ Данные арбитражной торговли между биржами Bitz - Huobi """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bitz_huobi'


class BitzCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Bitz - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bitz_coinex'


class BitzBibox(models.Model):
    """ Данные арбитражной торговли между биржами Bitz - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'bitz_bibox'


class HuobiCoinex(models.Model):
    """ Данные арбитражной торговли между биржами Huobi - Coinex """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'huobi_coinex'


class HuobiBibox(models.Model):
    """ Данные арбитражной торговли между биржами Huobi - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'huobi_bibox'


class CoinexBibox(models.Model):
    """ Данные арбитражной торговли между биржами Coinex - Bibox """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)

    class Meta:
        db_table = 'coinex_bibox'


class CoinListing(models.Model):
    """ Список новых монет, выходящих на биржах """
    exchange = models.CharField('Биржа', max_length=50, default=None, null=True)
    name = models.CharField('Монета', max_length=200, default=None, null=True)
    date = models.DateField('Дата', default=None, null=True)

    class Meta:
        db_table = 'coin_listing'


class ExchangeModel(models.Model):
    """ Базовая модель биржи """
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.FloatField('Объем рынка', default=None, null=True)

    class Meta:
        abstract = True


class Binance(ExchangeModel):
    """ Данные монет на бирже Binance """
    trading = models.CharField('Торговля', max_length=50, default=None, null=True)
    deposit = models.CharField('Пополнение', max_length=55, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=55, default=None, null=True)

    class Meta:
        db_table = 'binance'


class Bittrex(ExchangeModel):
    """ Данные монет на бирже Bittrex """
    trading = models.CharField('Объем рынка', max_length=50, default=None, null=True)

    class Meta:
        db_table = 'bittrex'


class Bibox(ExchangeModel):
    """ Данные монет на бирже Bibox """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)

    class Meta:
        db_table = 'bibox'


class Bitz(ExchangeModel):
    """ Данные монет на бирже Bitz """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)

    class Meta:
        db_table = 'bitz'


class Gateio(ExchangeModel):
    """ Данные монет на бирже Gateio """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)

    class Meta:
        db_table = 'gateio'


class Coinex(ExchangeModel):
    """ Данные монет на бирже Coinex """

    class Meta:
        db_table = 'coinex'


class Hitbtc(ExchangeModel):
    """ Данные монет на бирже Hitbtc """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)

    class Meta:
        db_table = 'hitbtc'


class Okex(ExchangeModel):
    """ Данные монет на бирже Okex """

    class Meta:
        db_table = 'okex'


class Huobi(ExchangeModel):
    """ Данные монет на бирже Huobi """
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)

    class Meta:
        db_table = 'huobi'


class Kraken(ExchangeModel):
    """ Данные монет на бирже Kraken """

    class Meta:
        db_table = 'kraken'


class Kucoin(ExchangeModel):
    """ Данные монет на бирже Kucoin """
    trading = models.CharField('Торговля', max_length=50, default=None, null=True)

    class Meta:
        db_table = 'kucoin'


class Poloniex(ExchangeModel):
    """ Данные монет на бирже Poloniex """
    trading = models.CharField('Торговля', max_length=50, default=None, null=True)
    blocks = models.IntegerField('Блоки', default=None, null=True)

    class Meta:
        db_table = 'poloniex'


class ExchangeUpdate(models.Model):
    """ Обновление бирж """
    exchange = models.CharField('Биржа', max_length=20, default=None, null=True)
    last_update = models.DateTimeField('Дата обновления', auto_now_add=True)
    status = models.BooleanField('Статус', default=False)

    class Meta:
        db_table = 'exchange_update'


class Trading(models.Model):
    """ Сигналы продажи выбранных пар монет по выбранным показателям дохода """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_trading_name', on_delete=models.CASCADE)
    exchange = models.CharField('Биржа', max_length=20, default=None, null=True)
    pair = models.CharField('Пара', max_length=20, default=None, null=True)
    amount = models.FloatField('Количество', default=0, null=True)
    price = models.FloatField('Цена', default=0, null=True)
    last_price = models.FloatField('Цена', default=0, null=True)
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

    class Meta:
        db_table = 'trading'
        verbose_name = 'Trading'
        verbose_name_plural = 'Trading'


class Tracking(models.Model):
    """ Отслеживание изменения показателей торговых пар монет на биржах """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_tracking_name', on_delete=models.CASCADE)
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

    class Meta:
        db_table = 'tracking'
        verbose_name = 'Tracking'
        verbose_name_plural = 'Tracking'


class UsersBalance(models.Model):
    """ Данные баланса пользователей """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_balance_name', on_delete=models.CASCADE)
    balance = models.TextField('Баланс', default=0, null=False)
    totalbtc = models.FloatField('TotalBTC', default=0, null=False)
    totalusd = models.FloatField('TotalUSD', default=0, null=False)

    class Meta:
        db_table = 'users_balance'
        verbose_name = 'Users Balance'
        verbose_name_plural = 'Users Balance'


class UsersKeys(models.Model):
    """ Секретные ключи пользователей для доступа на биржу """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_keys_name', on_delete=models.CASCADE)
    telegram = models.BigIntegerField('Telegram', default=0, null=False, blank=True)
    binance_key = models.CharField('Binance Key', max_length=80, default='', null=True, blank=True)
    binance_secret = models.CharField('Binance Secret', max_length=80, default='', null=True, blank=True)
    bittrex_key = models.CharField('Bittrex Key', max_length=80, default='', null=True, blank=True)
    bittrex_secret = models.CharField('Bittrex Secret', max_length=80, default='', null=True, blank=True)
    poloniex_key = models.CharField('Poloniex Key', max_length=80, default='', null=True, blank=True)
    poloniex_secret = models.CharField('Poloniex Secret', max_length=128, default='', null=True, blank=True)
    hitbtc_key = models.CharField('HitBTC Key', max_length=80, default='', null=True, blank=True)
    hitbtc_secret = models.CharField('HitBTC Secret', max_length=80, default='', null=True, blank=True)
    kucoin_key = models.CharField('Kucoin Key', max_length=80, default='', null=True, blank=True)
    kucoin_secret = models.CharField('Kucoin Secret', max_length=80, default='', null=True, blank=True)
    kucoin_password = models.CharField('Kucoin Password', max_length=80, default='', null=True, blank=True)
    kraken_key = models.CharField('Kraken Key', max_length=80, default='', null=True, blank=True)
    kraken_secret = models.CharField('Kraken Secret', max_length=100, default='', null=True, blank=True)
    huobi_key = models.CharField('Huobi Key', max_length=80, default='', null=True, blank=True)
    huobi_secret = models.CharField('Huobi Secret', max_length=80, default='', null=True, blank=True)
    okex_key = models.CharField('OKex Key', max_length=80, default='', null=True, blank=True)
    okex_secret = models.CharField('OKex Secret', max_length=80, default='', null=True, blank=True)
    okex_password = models.CharField('OKex Password', max_length=80, default='', null=True, blank=True)
    gateio_key = models.CharField('Gate.io Key', max_length=80, default='', null=True, blank=True)
    gateio_secret = models.CharField('Gate.io Secret', max_length=80, default='', null=True, blank=True)
    coinex_key = models.CharField('Coinex Key', max_length=80, default='', null=True, blank=True)
    coinex_secret = models.CharField('Coinex Secret', max_length=80, default='', null=True, blank=True)
    bitz_key = models.CharField('Bit-Z Key', max_length=80, default='', null=True, blank=True)
    bitz_secret = models.CharField('Bit-Z Secret', max_length=80, default='', null=True, blank=True)
    bibox_key = models.CharField('Bibox Key', max_length=80, default='', null=True, blank=True)
    bibox_secret = models.CharField('Bibox Secret', max_length=80, default='', null=True, blank=True)

    class Meta:
        db_table = 'users_keys'
        verbose_name = 'Users Keys'
        verbose_name_plural = 'Users Keys'


class UsersAccount(models.Model):
    """ Данные аккаунта пользователей """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_account_name', on_delete=models.CASCADE)
    last_pay_time = models.DateField('Дата последней оплаты', auto_now=True)
    days = models.IntegerField('Кол-во оплаченных дней', default=0, null=False)

    class Meta:
        db_table = 'users_account'
        verbose_name = 'Users Account'
        verbose_name_plural = 'Users Account'


class UsersPayments(models.Model):
    """ Данные оплаты пользователей """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_payments_name', on_delete=models.CASCADE)
    pay_time = models.DateField('Дата оплаты', auto_now_add=True)
    money = models.FloatField('Оплата', default=0, null=False)

    class Meta:
        db_table = 'users_payments'
        verbose_name = 'Users Payments'
        verbose_name_plural = 'Users Payments'


def create_profile(**kwargs):
    """ Создание записей в таблицах UsersKeys, UsersBalance при регистрации пользователя """
    if kwargs['created']:
        UsersKeys.objects.create(user=kwargs['instance'])
        UsersBalance.objects.create(user=kwargs['instance'])
        UsersAccount.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)


@admin.register(UsersPayments)
class UsersPaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'pay_time', 'money')


@admin.register(UsersAccount)
class UsersAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_pay_time', 'days')


@admin.register(UsersBalance)
class UsersBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'totalbtc', 'totalusd')


@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ('user', 'exchange', 'pair', 'price', 'pricechangevalue', 'pricechangeprocent', 'priceactive',
                    'volume', 'volumechangevalue', 'volumechangeprocent', 'volumeactive')


@admin.register(Trading)
class TradingAdmin(admin.ModelAdmin):
    list_display = ('user', 'exchange', 'pair', 'amount', 'price', 'last_price', 'stoploss', 'trailingstoploss',
                    'takeprofit', 'trailingtakeprofit', 'trailingtakeprofitprocent', 'active', 'stoplossvalue',
                    'stoplosstrailingvalue', 'takeprofitvalue', 'takeprofittrailingvalue')


@admin.register(UsersKeys)
class UsersKeysAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram', 'binance_key', 'binance_secret', 'bittrex_key', 'bittrex_secret',
                    'poloniex_key', 'poloniex_secret', 'hitbtc_key', 'hitbtc_secret', 'kucoin_key', 'kucoin_secret',
                    'kucoin_password', 'kraken_key', 'kraken_secret', 'huobi_key', 'huobi_secret', 'okex_key',
                    'okex_secret', 'okex_password', 'gateio_key', 'gateio_secret', 'coinex_key', 'coinex_secret',
                    'bitz_key', 'bitz_secret', 'bibox_key', 'bibox_secret')


admin.site.site_header = "Crypto Arbitrage"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to Crypto Arbitrage Admin Panel"
