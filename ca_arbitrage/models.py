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