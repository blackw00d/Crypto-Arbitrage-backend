from datetime import timedelta, date
from rest_framework import serializers
from .models import *
from django.conf import settings

exchanges = {
    'Binance': Binance,
    'Bittrex': Bittrex,
    'Poloniex': Poloniex,
    'HitBTC': Hitbtc,
    'Kucoin': Kucoin,
    'Kraken': Kraken,
    'Huobi': Huobi,
    'OKex': Okex,
    'Gate.io': Gateio,
    'Coinex': Coinex,
    'Bit-Z': Bitz,
    'Bibox': Bibox
}


class BinanceBittrexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('bittrexlink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='bittrex_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    class Meta:
        model = BinanceBittrex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinanceHitbtcSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('hitbtclink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='hitbtc_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    class Meta:
        model = BinanceHitbtc
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinanceKucoinSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('kucoinlink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='kucoin_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    class Meta:
        model = BinanceKucoin
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinancePoloniexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('poloniexlink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='poloniex_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    class Meta:
        model = BinancePoloniex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinanceKrakenSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('krakenlink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='kraken_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    class Meta:
        model = BinanceKraken
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinanceOkexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('okexlink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='okex_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = BinanceOkex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinanceGateioSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('gateiolink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='gateio_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = BinanceGateio
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinanceBitzSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('bitzlink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='bitz_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = BinanceBitz
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinanceHuobiSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('huobilink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='huobi_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = BinanceHuobi
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinanceCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='coinex_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = BinanceCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BinanceBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('binancelink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='binance_price')
    price_b = serializers.CharField(source='bibox_price')

    def binancelink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://www.binance.com/ru/trade/{namea}_{name[0]}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = BinanceBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexHitbtcSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('hitbtclink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='hitbtc_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    class Meta:
        model = BittrexHitbtc
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexKucoinSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('kucoinlink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='kucoin_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    class Meta:
        model = BittrexKucoin
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexPoloniexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('poloniexlink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='poloniex_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    class Meta:
        model = BittrexPoloniex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexKrakenSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('krakenlink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='kraken_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    class Meta:
        model = BittrexKraken
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexOkexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('okexlink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='okex_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = BittrexOkex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexGateioSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('gateiolink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='gateio_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = BittrexGateio
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexBitzSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('bitzlink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='bitz_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = BittrexBitz
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexHuobiSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('huobilink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='huobi_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = BittrexHuobi
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='coinex_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = BittrexCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BittrexBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bittrexlink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='bittrex_price')
    price_b = serializers.CharField(source='bibox_price')

    def bittrexlink(self, exchange):
        name = exchange.name.split('-', 1)
        namea = "BCC" if name[1] == "BCH" else name[1]
        link = f'https://bittrex.com/Market/Index?MarketName={name[0]}-{namea}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = BittrexBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class PoloniexHitbtcSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('poloniexlink')
    link_b = serializers.SerializerMethodField('hitbtclink')
    price_a = serializers.CharField(source='poloniex_price')
    price_b = serializers.CharField(source='hitbtc_price')

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    class Meta:
        model = PoloniexHitbtc
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class PoloniexKucoinSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('poloniexlink')
    link_b = serializers.SerializerMethodField('kucoinlink')
    price_a = serializers.CharField(source='poloniex_price')
    price_b = serializers.CharField(source='kucoin_price')

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    class Meta:
        model = PoloniexKucoin
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class PoloniexKrakenSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('poloniexlink')
    link_b = serializers.SerializerMethodField('krakenlink')
    price_a = serializers.CharField(source='poloniex_price')
    price_b = serializers.CharField(source='kraken_price')

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    class Meta:
        model = PoloniexKraken
        fields = (
            'name', 'price_a', 'poloniex_volume', 'price_b', 'kraken_volume', 'profit', 'link_a',
            'link_b')


class PoloniexOkexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('poloniexlink')
    link_b = serializers.SerializerMethodField('okexlink')
    price_a = serializers.CharField(source='poloniex_price')
    price_b = serializers.CharField(source='okex_price')

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = PoloniexOkex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class PoloniexGateioSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('poloniexlink')
    link_b = serializers.SerializerMethodField('gateiolink')
    price_a = serializers.CharField(source='poloniex_price')
    price_b = serializers.CharField(source='gateio_price')

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = PoloniexGateio
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class PoloniexBitzSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('poloniexlink')
    link_b = serializers.SerializerMethodField('bitzlink')
    price_a = serializers.CharField(source='poloniex_price')
    price_b = serializers.CharField(source='bitz_price')

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = PoloniexBitz
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class PoloniexHuobiSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('poloniexlink')
    link_b = serializers.SerializerMethodField('huobilink')
    price_a = serializers.CharField(source='poloniex_price')
    price_b = serializers.CharField(source='huobi_price')

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobipro.com/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = PoloniexHuobi
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class PoloniexCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('poloniexlink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='poloniex_price')
    price_b = serializers.CharField(source='coinex_price')

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = PoloniexCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class PoloniexBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('poloniexlink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='poloniex_price')
    price_b = serializers.CharField(source='bibox_price')

    def poloniexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://poloniex.com/exchange#{name[0]}_{name[1]}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = PoloniexBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HitbtcKucoinSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('hitbtclink')
    link_b = serializers.SerializerMethodField('kucoinlink')
    price_a = serializers.CharField(source='hitbtc_price')
    price_b = serializers.CharField(source='kucoin_price')

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    class Meta:
        model = HitbtcKucoin
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HitbtckrakenSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('hitbtclink')
    link_b = serializers.SerializerMethodField('krakenlink')
    price_a = serializers.CharField(source='hitbtc_price')
    price_b = serializers.CharField(source='kraken_price')

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    class Meta:
        model = Hitbtckraken
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HitbtcOkexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('hitbtclink')
    link_b = serializers.SerializerMethodField('okexlink')
    price_a = serializers.CharField(source='hitbtc_price')
    price_b = serializers.CharField(source='okex_price')

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = HitbtcOkex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HitbtcGateioSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('hitbtclink')
    link_b = serializers.SerializerMethodField('gateiolink')
    price_a = serializers.CharField(source='hitbtc_price')
    price_b = serializers.CharField(source='gateio_price')

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = HitbtcGateio
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HitbtcBitzSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('hitbtclink')
    link_b = serializers.SerializerMethodField('bitzlink')
    price_a = serializers.CharField(source='hitbtc_price')
    price_b = serializers.CharField(source='bitz_price')

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = HitbtcBitz
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HitbtcHuobiSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('hitbtclink')
    link_b = serializers.SerializerMethodField('huobilink')
    price_a = serializers.CharField(source='hitbtc_price')
    price_b = serializers.CharField(source='huobi_price')

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = HitbtcHuobi
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HitbtcCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('hitbtclink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='hitbtc_price')
    price_b = serializers.CharField(source='coinex_price')

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = HitbtcCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HitbtcBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('hitbtclink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='hitbtc_price')
    price_b = serializers.CharField(source='bibox_price')

    def hitbtclink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://hitbtc.com/exchange/{name[1]}-to-{name[0]}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = HitbtcBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KucoinKrakenSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('kucoinlink')
    link_b = serializers.SerializerMethodField('krakenlink')
    price_a = serializers.CharField(source='kucoin_price')
    price_b = serializers.CharField(source='kraken_price')

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    class Meta:
        model = KucoinKraken
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KucoinOkexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('kucoinlink')
    link_b = serializers.SerializerMethodField('okexlink')
    price_a = serializers.CharField(source='kucoin_price')
    price_b = serializers.CharField(source='okex_price')

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = KucoinOkex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KucoinGateioSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('kucoinlink')
    link_b = serializers.SerializerMethodField('gateiolink')
    price_a = serializers.CharField(source='kucoin_price')
    price_b = serializers.CharField(source='gateio_price')

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = KucoinGateio
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KucoinBitzSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('kucoinlink')
    link_b = serializers.SerializerMethodField('bitzlink')
    price_a = serializers.CharField(source='kucoin_price')
    price_b = serializers.CharField(source='bitz_price')

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = KucoinBitz
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KucoinHuobiSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('kucoinlink')
    link_b = serializers.SerializerMethodField('huobilink')
    price_a = serializers.CharField(source='kucoin_price')
    price_b = serializers.CharField(source='huobi_price')

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = KucoinHuobi
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KucoinCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('kucoinlink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='kucoin_price')
    price_b = serializers.CharField(source='coinex_price')

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = KucoinCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KucoinBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('kucoinlink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='kucoin_price')
    price_b = serializers.CharField(source='bibox_price')

    def kucoinlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kucoin.com/{name[1]}-{name[0]}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = KucoinBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KrakenOkexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('krakenlink')
    link_b = serializers.SerializerMethodField('okexlink')
    price_a = serializers.CharField(source='kraken_price')
    price_b = serializers.CharField(source='okex_price')

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = KrakenOkex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KrakenGateioSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('krakenlink')
    link_b = serializers.SerializerMethodField('gateiolink')
    price_a = serializers.CharField(source='kraken_price')
    price_b = serializers.CharField(source='gateio_price')

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = KrakenGateio
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KrakenBitzSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('krakenlink')
    link_b = serializers.SerializerMethodField('bitzlink')
    price_a = serializers.CharField(source='kraken_price')
    price_b = serializers.CharField(source='bitz_price')

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = KrakenBitz
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KrakenHuobiSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('krakenlink')
    link_b = serializers.SerializerMethodField('huobilink')
    price_a = serializers.CharField(source='kraken_price')
    price_b = serializers.CharField(source='huobi_price')

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = KrakenHuobi
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KrakenCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('krakenlink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='kraken_price')
    price_b = serializers.CharField(source='coinex_price')

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = KrakenCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class KrakenBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('krakenlink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='kraken_price')
    price_b = serializers.CharField(source='bibox_price')

    def krakenlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://trade.kraken.com/markets/kraken/{name[1].lower()}/{name[0].lower()}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = KrakenBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class OkexGateioSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('okexlink')
    link_b = serializers.SerializerMethodField('gateiolink')
    price_a = serializers.CharField(source='okex_price')
    price_b = serializers.CharField(source='gateio_price')

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = OkexGateio
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class OkexBitzSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('okexlink')
    link_b = serializers.SerializerMethodField('bitzlink')
    price_a = serializers.CharField(source='okex_price')
    price_b = serializers.CharField(source='bitz_price')

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = OkexBitz
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class OkexHuobiSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('okexlink')
    link_b = serializers.SerializerMethodField('huobilink')
    price_a = serializers.CharField(source='okex_price')
    price_b = serializers.CharField(source='huobi_price')

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = OkexHuobi
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class OkexCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('okexlink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='okex_price')
    price_b = serializers.CharField(source='coinex_price')

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = OkexCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class OkexBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('okexlink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='okex_price')
    price_b = serializers.CharField(source='bibox_price')

    def okexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.okex.com/spot/trade#product={name[1].lower()}_{name[0].lower()}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = OkexBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class GateioBitzSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('gateiolink')
    link_b = serializers.SerializerMethodField('bitzlink')
    price_a = serializers.CharField(source='gateio_price')
    price_b = serializers.CharField(source='bitz_price')

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = GateioBitz
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class GateioHuobiSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('gateiolink')
    link_b = serializers.SerializerMethodField('huobilink')
    price_a = serializers.CharField(source='gateio_price')
    price_b = serializers.CharField(source='huobi_price')

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = GateioHuobi
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class GateioCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('gateiolink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='gateio_price')
    price_b = serializers.CharField(source='coinex_price')

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = GateioCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class GateioBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('gateiolink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='gateio_price')
    price_b = serializers.CharField(source='bibox_price')

    def gateiolink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://gate.io/trade/{name[1].lower()}_{name[0].lower()}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = GateioBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BitzHuobiSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bitzlink')
    link_b = serializers.SerializerMethodField('huobilink')
    price_a = serializers.CharField(source='bitz_price')
    price_b = serializers.CharField(source='huobi_price')

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    class Meta:
        model = BitzHuobi
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BitzCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bitzlink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='bitz_price')
    price_b = serializers.CharField(source='coinex_price')

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = BitzCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class BitzBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('bitzlink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='bitz_price')
    price_b = serializers.CharField(source='bibox_price')

    def bitzlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bit-z.com/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = BitzBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HuobiCoinexSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('huobilink')
    link_b = serializers.SerializerMethodField('coinexlink')
    price_a = serializers.CharField(source='huobi_price')
    price_b = serializers.CharField(source='coinex_price')

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    class Meta:
        model = HuobiCoinex
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class HuobiBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('huobilink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='huobi_price')
    price_b = serializers.CharField(source='bibox_price')

    def huobilink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.huobi.fm/ru-ru/exchange/{name[1].lower()}_{name[0].lower()}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = HuobiBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class CoinexBiboxSerializer(serializers.ModelSerializer):
    link_a = serializers.SerializerMethodField('coinexlink')
    link_b = serializers.SerializerMethodField('biboxlink')
    price_a = serializers.CharField(source='coinex_price')
    price_b = serializers.CharField(source='bibox_price')

    def coinexlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.coinex.com/exchange?currency={name[0].lower()}&dest={name[1].lower()}'
        return link

    def biboxlink(self, exchange):
        name = exchange.name.split('-', 1)
        link = f'https://www.bibox.com/exchange?coinPair={name[1]}_{name[0]}'
        return link

    class Meta:
        model = CoinexBibox
        fields = ('name', 'price_a', 'price_b', 'profit', 'link_a', 'link_b')


class ArbitrageSerializers(serializers.Serializer):
    binance_bittrex = BinanceBittrexSerializer(many=True)
    binance_hitbtc = BinanceHitbtcSerializer(many=True)
    binance_kucoin = BinanceKucoinSerializer(many=True)
    binance_poloniex = BinancePoloniexSerializer(many=True)
    binance_kraken = BinanceKrakenSerializer(many=True)
    binance_okex = BinanceOkexSerializer(many=True)
    binance_gateio = BinanceGateioSerializer(many=True)
    binance_bitz = BinanceBitzSerializer(many=True)
    binance_huobi = BinanceHuobiSerializer(many=True)
    binance_coinex = BinanceCoinexSerializer(many=True)
    binance_bibox = BinanceBiboxSerializer(many=True)
    bittrex_hitbtc = BittrexHitbtcSerializer(many=True)
    bittrex_kucoin = BittrexKucoinSerializer(many=True)
    bittrex_poloniex = BittrexPoloniexSerializer(many=True)
    bittrex_kraken = BittrexKrakenSerializer(many=True)
    bittrex_okex = BittrexOkexSerializer(many=True)
    bittrex_gateio = BittrexGateioSerializer(many=True)
    bittrex_bitz = BittrexBitzSerializer(many=True)
    bittrex_huobi = BittrexHuobiSerializer(many=True)
    bittrex_coinex = BittrexCoinexSerializer(many=True)
    bittrex_bibox = BittrexBiboxSerializer(many=True)
    poloniex_hitbtc = PoloniexHitbtcSerializer(many=True)
    poloniex_kucoin = PoloniexKucoinSerializer(many=True)
    poloniex_kraken = PoloniexKrakenSerializer(many=True)
    poloniex_okex = PoloniexOkexSerializer(many=True)
    poloniex_gateio = PoloniexGateioSerializer(many=True)
    poloniex_bitz = PoloniexBitzSerializer(many=True)
    poloniex_huobi = PoloniexHuobiSerializer(many=True)
    poloniex_coinex = PoloniexCoinexSerializer(many=True)
    poloniex_bibox = PoloniexBiboxSerializer(many=True)
    hitbtc_kucoin = HitbtcKucoinSerializer(many=True)
    hitbtc_kraken = HitbtckrakenSerializer(many=True)
    hitbtc_okex = HitbtcOkexSerializer(many=True)
    hitbtc_gateio = HitbtcGateioSerializer(many=True)
    hitbtc_bitz = HitbtcBitzSerializer(many=True)
    hitbtc_huobi = HitbtcHuobiSerializer(many=True)
    hitbtc_coinex = HitbtcCoinexSerializer(many=True)
    hitbtc_bibox = HitbtcBiboxSerializer(many=True)
    kucoin_kraken = KucoinKrakenSerializer(many=True)
    kucoin_okex = KucoinOkexSerializer(many=True)
    kucoin_gateio = KucoinGateioSerializer(many=True)
    kucoin_bitz = KucoinBitzSerializer(many=True)
    kucoin_huobi = KucoinHuobiSerializer(many=True)
    kucoin_coinex = KucoinCoinexSerializer(many=True)
    kucoin_bibox = KucoinBiboxSerializer(many=True)
    kraken_okex = KrakenOkexSerializer(many=True)
    kraken_gateio = KrakenGateioSerializer(many=True)
    kraken_bitz = KrakenBitzSerializer(many=True)
    kraken_huobi = KrakenHuobiSerializer(many=True)
    kraken_coinex = KrakenCoinexSerializer(many=True)
    kraken_bibox = KrakenBiboxSerializer(many=True)
    okex_gateio = OkexGateioSerializer(many=True)
    okex_bitz = OkexBitzSerializer(many=True)
    okex_huobi = OkexHuobiSerializer(many=True)
    okex_coinex = OkexCoinexSerializer(many=True)
    okex_bibox = OkexBiboxSerializer(many=True)
    gateio_bitz = GateioBitzSerializer(many=True)
    gateio_huobi = GateioHuobiSerializer(many=True)
    gateio_coinex = GateioCoinexSerializer(many=True)
    gateio_bibox = GateioBiboxSerializer(many=True)
    bitz_huobi = BitzHuobiSerializer(many=True)
    bitz_coinex = BitzCoinexSerializer(many=True)
    bitz_bibox = BitzBiboxSerializer(many=True)
    huobi_coinex = HuobiCoinexSerializer(many=True)
    huobi_bibox = HuobiBiboxSerializer(many=True)
    coinex_bibox = CoinexBiboxSerializer(many=True)


class CoinListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinListing
        fields = ('exchange', 'name', 'date')


class BinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Binance
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume', 'trading', 'deposit', 'withdraw',)


class BittrexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bittrex
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume', 'trading',)


class KucoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kucoin
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume', 'trading',)


class HitbtcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hitbtc
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume', 'deposit', 'withdraw',)


class PoloniexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poloniex
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume', 'trading', 'blocks',)


class KrakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kraken
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume',)


class HuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huobi
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume', 'deposit', 'withdraw',)


class OkexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Okex
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume',)


class GateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateio
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume', 'deposit', 'withdraw',)


class CoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coinex
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume',)


class BitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitz
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume', 'deposit', 'withdraw',)


class BiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibox
        exclude = ('id', 'id_name', 'ask_volume', 'bid_volume', 'deposit', 'withdraw',)


class ExchangeUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExchangeUpdate
        fields = ('last_update',)


class ExchangesSerializers(serializers.Serializer):
    binance = BinanceSerializer(many=True)
    bittrex = BittrexSerializer(many=True)
    poloniex = PoloniexSerializer(many=True)
    hitbtc = HitbtcSerializer(many=True)
    kucoin = KucoinSerializer(many=True)
    kraken = KrakenSerializer(many=True)
    huobi = HuobiSerializer(many=True)
    okex = OkexSerializer(many=True)
    gateio = GateioSerializer(many=True)
    coinex = CoinexSerializer(many=True)
    bitz = BitzSerializer(many=True)
    bibox = BiboxSerializer(many=True)


class TradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trading
        fields = (
            'id', 'user', 'exchange', 'pair', 'amount', 'price', 'last_price', 'stoploss', 'trailingstoploss',
            'takeprofit', 'trailingtakeprofit', 'trailingtakeprofitprocent', 'active', 'stoplossvalue',
            'stoplosstrailingvalue', 'takeprofitvalue', 'takeprofittrailingvalue')


class TradingServerSerializer(serializers.ModelSerializer):
    price_now = serializers.SerializerMethodField('price_now_value')
    user_telegram = serializers.SerializerMethodField('user_telegram_value')

    def price_now_value(self, exchange):
        return exchanges[exchange.exchange].objects.get(name=exchange.pair).price

    def user_telegram_value(self, exchange):
        return UsersKeys.objects.get(user_id=exchange.user_id).telegram

    class Meta:
        model = Trading
        fields = (
            'id', 'user', 'user_telegram', 'exchange', 'pair', 'amount', 'price', 'last_price', 'price_now',
            'stoploss', 'trailingstoploss', 'takeprofit', 'trailingtakeprofit', 'trailingtakeprofitprocent',
            'active', 'stoplossvalue', 'stoplosstrailingvalue', 'takeprofitvalue', 'takeprofittrailingvalue')


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = ('id', 'user', 'exchange', 'pair', 'price', 'pricechangevalue',
                  'pricechangeprocent', 'priceactive', 'volume', 'volumechangevalue',
                  'volumechangeprocent', 'volumeactive')


class TrackingServerSerializer(serializers.ModelSerializer):
    price_now = serializers.SerializerMethodField('price_now_value')
    volume_now = serializers.SerializerMethodField('volume_now_value')
    user_telegram = serializers.SerializerMethodField('user_telegram_value')

    def price_now_value(self, exchange):
        return exchanges[exchange.exchange].objects.get(name=exchange.pair).price

    def volume_now_value(self, exchange):
        return exchanges[exchange.exchange].objects.get(name=exchange.pair).volume

    def user_telegram_value(self, exchange):
        return UsersKeys.objects.get(user_id=exchange.user_id).telegram

    class Meta:
        model = Tracking
        fields = ('id', 'user', 'user_telegram', 'exchange', 'pair', 'price', 'price_now', 'pricechangevalue',
                  'pricechangeprocent', 'priceactive', 'volume', 'volume_now', 'volumechangevalue',
                  'volumechangeprocent', 'volumeactive')


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersBalance
        fields = ('balance', 'totalbtc', 'totalusd')


class UserKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersKeys
        fields = ('user', 'telegram', 'binance_key', 'binance_secret', 'bittrex_key', 'bittrex_secret', 'poloniex_key',
                  'poloniex_secret', 'hitbtc_key', 'hitbtc_secret', 'kucoin_key', 'kucoin_secret', 'kucoin_password',
                  'kraken_key', 'kraken_secret', 'huobi_key', 'huobi_secret', 'okex_key', 'okex_secret',
                  'okex_password', 'gateio_key', 'gateio_secret', 'coinex_key', 'coinex_secret', 'bitz_key',
                  'bitz_secret', 'bibox_key', 'bibox_secret')


class UsersAccountSerializer(serializers.ModelSerializer):
    deadline = serializers.SerializerMethodField('deadline_value')
    days_to_deadline = serializers.SerializerMethodField('days_to_deadline_value')

    def deadline_value(self, data):
        return data.last_pay_time + timedelta(days=data.days)

    def days_to_deadline_value(self, data):
        difference = data.last_pay_time - date.today() + timedelta(days=data.days)
        return difference.days if data.days > 0 else 0

    class Meta:
        model = UsersAccount
        fields = ('last_pay_time', 'days_to_deadline', 'deadline', 'days')


class UsersPaymentsSerializer(serializers.ModelSerializer):
    pay_days = serializers.SerializerMethodField('days_value')

    def days_value(self, data):
        if data.money == settings.PAYMENT:
            return 30
        elif data.money == settings.PAYMENT * 2.75:
            return 3 * 30
        elif data.money == settings.PAYMENT * 5:
            return 6 * 30
        return data.money / settings.PAYMENT * 30

    class Meta:
        model = UsersPayments
        fields = ('user', 'pay_time', 'money', 'pay_days')
