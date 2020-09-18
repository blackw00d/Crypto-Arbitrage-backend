from django.db import models


class BinanceBittrex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceHitbtc(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceKucoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceLivecoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinancePoloniex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceKraken(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceOkex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceGateio(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceBitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BinanceBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    binance_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    binance_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexHitbtc(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexKucoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexLivecoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexPoloniex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexKraken(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexOkex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexGateio(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexBitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BittrexBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bittrex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bittrex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexHitbtc(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexKucoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexLivecoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexKraken(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexOkex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexGateio(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexBitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class PoloniexBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    poloniex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    poloniex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcKucoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcLivecoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class Hitbtckraken(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcOkex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcGateio(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcBitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HitbtcBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    hitbtc_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    hitbtc_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinLivecoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinKraken(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinOkex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinGateio(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinBitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KucoinBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kucoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kucoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class LivecoinKraken(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class LivecoinOkex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class LivecoinGateio(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class LivecoinBitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class LivecoinHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class LivecoinCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class LivecoinBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    livecoin_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    livecoin_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenOkex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenGateio(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenBitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class KrakenBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    kraken_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    kraken_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexGateio(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexBitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class OkexBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    okex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    okex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class GateioBitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class GateioHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class GateioCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class GateioBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    gateio_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    gateio_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BitzHuobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BitzCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class BitzBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    bitz_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    bitz_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HuobiCoinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class HuobiBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    huobi_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    huobi_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class CoinexBibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    coinex_price = models.CharField('Цена Binance', max_length=50, default=None, null=True)
    bibox_price = models.CharField('Цена Bibox', max_length=50, default=None, null=True)
    coinex_volume = models.CharField('Объем Binance', max_length=50, default=None, null=True)
    bibox_volume = models.CharField('Объем Bibox', max_length=50, default=None, null=True)
    profit = models.FloatField('Профит', default=None, null=True)


class UserBalance(models.Model):
    user = models.CharField('Имя', max_length=50, default=None, null=True)
    balance = models.TextField('Баланс', default=None, null=True)
    totalbtc = models.FloatField('TotalBTC', default=None, null=True)
    totalusd = models.FloatField('TotalUSD', default=None, null=True)


class CoinListing(models.Model):
    exchange = models.CharField('Биржа', max_length=50, default=None, null=True)
    name = models.CharField('Монета', max_length=200, default=None, null=True)
    date = models.DateField('Дата', default=None, null=True)


class Binance(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    trading = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    deposit = models.CharField('Пополнение', max_length=55, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=55, default=None, null=True)


class Bittrex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    trading = models.CharField('Объем рынка', max_length=50, default=None, null=True)


class Bibox(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)


class Bitz(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)


class Coinex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)


class Gateio(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)


class Hitbtc(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)
    blocks = models.IntegerField('Блоки', default=None, null=True)


class Okex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)


class Huobi(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    deposit = models.CharField('Пополнение', max_length=50, default=None, null=True)
    withdraw = models.CharField('Вывод', max_length=50, default=None, null=True)


class Kraken(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)


class Kucoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    trading = models.CharField('Торговля', max_length=50, default=None, null=True)


class Livecoin(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    trading = models.CharField('Торговля', max_length=50, default=None, null=True)


class Poloniex(models.Model):
    name = models.CharField('Имя', max_length=50, default=None, null=True)
    id_name = models.CharField('Монета', max_length=50, default=None, null=True)
    price = models.FloatField('Цена', default=None, null=True)
    ask = models.FloatField('Цена продажи', default=None, null=True)
    ask_volume = models.FloatField('Объем продажи', default=None, null=True)
    bid = models.FloatField('Цена покупки', default=None, null=True)
    bid_volume = models.FloatField('Объем покупки', default=None, null=True)
    volume = models.CharField('Объем рынка', max_length=50, default=None, null=True)
    trading = models.CharField('Торговля', max_length=50, default=None, null=True)
    blocks = models.IntegerField('Блоки', default=None, null=True)
