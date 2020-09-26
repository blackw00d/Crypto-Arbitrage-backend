from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class BalanceView(APIView):
    """ БАЛАНС """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        balance = UserBalance.objects.get(user=request.data)
        serializer = BalanceSerializer(balance)
        return Response(serializer.data)


class ListingView(APIView):
    """ ЛИСТИНГ МОНЕТ """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        listing = CoinListing.objects.all().order_by('date')
        serializer = CoinListingSerializer(listing, many=True)
        return Response(serializer.data)


class ExchangesView(APIView):
    """ ВЫВОД ДАННЫХ БИРЖ """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
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
        return Response(serializer.data)


class ArbitrageView(APIView):
    """ АРБИТРАЖ """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        filters = {}
        MinVolume = 30000
        MinProfit = 0.01
        MaxProfit = 100
        filters['binance_bittrex'] = BinanceBittrex.objects.filter(binance_volume__gt=MinVolume,
                                                                   bittrex_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['binance_hitbtc'] = BinanceHitbtc.objects.filter(binance_volume__gt=MinVolume,
                                                                 hitbtc_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['binance_kucoin'] = BinanceKucoin.objects.filter(binance_volume__gt=MinVolume,
                                                                 kucoin_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['binance_livecoin'] = BinanceLivecoin.objects.filter(binance_volume__gt=MinVolume,
                                                                     livecoin_volume__gt=MinVolume,
                                                                     profit__gt=MinProfit,
                                                                     profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['binance_poloniex'] = BinancePoloniex.objects.filter(binance_volume__gt=MinVolume,
                                                                     poloniex_volume__gt=MinVolume,
                                                                     profit__gt=MinProfit,
                                                                     profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['binance_kraken'] = BinanceKraken.objects.filter(binance_volume__gt=MinVolume,
                                                                 kraken_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['binance_okex'] = BinanceOkex.objects.filter(binance_volume__gt=MinVolume, okex_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['binance_gateio'] = BinanceGateio.objects.filter(binance_volume__gt=MinVolume,
                                                                 gateio_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['binance_bitz'] = BinanceBitz.objects.filter(binance_volume__gt=MinVolume, bitz_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['binance_huobi'] = BinanceHuobi.objects.filter(binance_volume__gt=MinVolume, huobi_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['binance_coinex'] = BinanceCoinex.objects.filter(binance_volume__gt=MinVolume,
                                                                 coinex_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['binance_bibox'] = BinanceBibox.objects.filter(binance_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['bittrex_hitbtc'] = BittrexHitbtc.objects.filter(bittrex_volume__gt=MinVolume,
                                                                 hitbtc_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['bittrex_kucoin'] = BittrexKucoin.objects.filter(bittrex_volume__gt=MinVolume,
                                                                 kucoin_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['bittrex_livecoin'] = BittrexLivecoin.objects.filter(bittrex_volume__gt=MinVolume,
                                                                     livecoin_volume__gt=MinVolume,
                                                                     profit__gt=MinProfit,
                                                                     profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['bittrex_poloniex'] = BittrexPoloniex.objects.filter(bittrex_volume__gt=MinVolume,
                                                                     poloniex_volume__gt=MinVolume,
                                                                     profit__gt=MinProfit,
                                                                     profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['bittrex_kraken'] = BittrexKraken.objects.filter(bittrex_volume__gt=MinVolume,
                                                                 kraken_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['bittrex_okex'] = BittrexOkex.objects.filter(bittrex_volume__gt=MinVolume, okex_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['bittrex_gateio'] = BittrexGateio.objects.filter(bittrex_volume__gt=MinVolume,
                                                                 gateio_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['bittrex_bitz'] = BittrexBitz.objects.filter(bittrex_volume__gt=MinVolume, bitz_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['bittrex_huobi'] = BittrexHuobi.objects.filter(bittrex_volume__gt=MinVolume, huobi_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['bittrex_coinex'] = BittrexCoinex.objects.filter(bittrex_volume__gt=MinVolume,
                                                                 coinex_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['bittrex_bibox'] = BittrexBibox.objects.filter(bittrex_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['poloniex_hitbtc'] = PoloniexHitbtc.objects.filter(poloniex_volume__gt=MinVolume,
                                                                   hitbtc_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['poloniex_kucoin'] = PoloniexKucoin.objects.filter(poloniex_volume__gt=MinVolume,
                                                                   kucoin_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['poloniex_livecoin'] = PoloniexLivecoin.objects.filter(poloniex_volume__gt=MinVolume,
                                                                       livecoin_volume__gt=MinVolume,
                                                                       profit__gt=MinProfit,
                                                                       profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['poloniex_kraken'] = PoloniexKraken.objects.filter(poloniex_volume__gt=MinVolume,
                                                                   kraken_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['poloniex_okex'] = PoloniexOkex.objects.filter(poloniex_volume__gt=MinVolume, okex_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['poloniex_gateio'] = PoloniexGateio.objects.filter(poloniex_volume__gt=MinVolume,
                                                                   gateio_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['poloniex_bitz'] = PoloniexBitz.objects.filter(poloniex_volume__gt=MinVolume, bitz_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['poloniex_huobi'] = PoloniexHuobi.objects.filter(poloniex_volume__gt=MinVolume,
                                                                 huobi_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['poloniex_coinex'] = PoloniexCoinex.objects.filter(poloniex_volume__gt=MinVolume,
                                                                   coinex_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['poloniex_bibox'] = PoloniexBibox.objects.filter(poloniex_volume__gt=MinVolume,
                                                                 bibox_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['hitbtc_kucoin'] = HitbtcKucoin.objects.filter(hitbtc_volume__gt=MinVolume, kucoin_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['hitbtc_livecoin'] = HitbtcLivecoin.objects.filter(hitbtc_volume__gt=MinVolume,
                                                                   livecoin_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['hitbtc_kraken'] = Hitbtckraken.objects.filter(hitbtc_volume__gt=MinVolume, kraken_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['hitbtc_okex'] = HitbtcOkex.objects.filter(hitbtc_volume__gt=MinVolume, okex_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['hitbtc_gateio'] = HitbtcGateio.objects.filter(hitbtc_volume__gt=MinVolume, gateio_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['hitbtc_bitz'] = HitbtcBitz.objects.filter(hitbtc_volume__gt=MinVolume, bitz_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['hitbtc_huobi'] = HitbtcHuobi.objects.filter(hitbtc_volume__gt=MinVolume, huobi_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['hitbtc_coinex'] = HitbtcCoinex.objects.filter(hitbtc_volume__gt=MinVolume, coinex_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['hitbtc_bibox'] = HitbtcBibox.objects.filter(hitbtc_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kucoin_livecoin'] = KucoinLivecoin.objects.filter(kucoin_volume__gt=MinVolume,
                                                                   livecoin_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['kucoin_kraken'] = KucoinKraken.objects.filter(kucoin_volume__gt=MinVolume, kraken_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kucoin_okex'] = KucoinOkex.objects.filter(kucoin_volume__gt=MinVolume, okex_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kucoin_gateio'] = KucoinGateio.objects.filter(kucoin_volume__gt=MinVolume, gateio_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kucoin_bitz'] = KucoinBitz.objects.filter(kucoin_volume__gt=MinVolume, bitz_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kucoin_huobi'] = KucoinHuobi.objects.filter(kucoin_volume__gt=MinVolume, huobi_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kucoin_coinex'] = KucoinCoinex.objects.filter(kucoin_volume__gt=MinVolume, coinex_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kucoin_bibox'] = KucoinBibox.objects.filter(kucoin_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['livecoin_kraken'] = LivecoinKraken.objects.filter(livecoin_volume__gt=MinVolume,
                                                                   kraken_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['livecoin_okex'] = LivecoinOkex.objects.filter(livecoin_volume__gt=MinVolume, okex_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['livecoin_gateio'] = LivecoinGateio.objects.filter(livecoin_volume__gt=MinVolume,
                                                                   gateio_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['livecoin_bitz'] = LivecoinBitz.objects.filter(livecoin_volume__gt=MinVolume, bitz_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['livecoin_huobi'] = LivecoinHuobi.objects.filter(livecoin_volume__gt=MinVolume,
                                                                 huobi_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['livecoin_coinex'] = LivecoinCoinex.objects.filter(livecoin_volume__gt=MinVolume,
                                                                   coinex_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                   profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['livecoin_bibox'] = LivecoinBibox.objects.filter(livecoin_volume__gt=MinVolume,
                                                                 bibox_volume__gt=MinVolume, profit__gt=MinProfit,
                                                                 profit__lt=MaxProfit).order_by('name').order_by(
            '-profit')
        filters['kraken_okex'] = KrakenOkex.objects.filter(kraken_volume__gt=MinVolume, okex_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kraken_gateio'] = KrakenGateio.objects.filter(kraken_volume__gt=MinVolume, gateio_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kraken_bitz'] = KrakenBitz.objects.filter(kraken_volume__gt=MinVolume, bitz_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kraken_huobi'] = KrakenHuobi.objects.filter(kraken_volume__gt=MinVolume, huobi_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kraken_coinex'] = KrakenCoinex.objects.filter(kraken_volume__gt=MinVolume, coinex_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['kraken_bibox'] = KrakenBibox.objects.filter(kraken_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['okex_gateio'] = OkexGateio.objects.filter(okex_volume__gt=MinVolume, gateio_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['okex_bitz'] = OkexBitz.objects.filter(okex_volume__gt=MinVolume, bitz_volume__gt=MinVolume,
                                                       profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['okex_huobi'] = OkexHuobi.objects.filter(okex_volume__gt=MinVolume, huobi_volume__gt=MinVolume,
                                                         profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['okex_coinex'] = OkexCoinex.objects.filter(okex_volume__gt=MinVolume, coinex_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['okex_bibox'] = OkexBibox.objects.filter(okex_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                         profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['gateio_bitz'] = GateioBitz.objects.filter(gateio_volume__gt=MinVolume, bitz_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['gateio_huobi'] = GateioHuobi.objects.filter(gateio_volume__gt=MinVolume, huobi_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['gateio_coinex'] = GateioCoinex.objects.filter(gateio_volume__gt=MinVolume, coinex_volume__gt=MinVolume,
                                                               profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['gateio_bibox'] = GateioBibox.objects.filter(gateio_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['bitz_huobi'] = BitzHuobi.objects.filter(bitz_volume__gt=MinVolume, huobi_volume__gt=MinVolume,
                                                         profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['bitz_coinex'] = BitzCoinex.objects.filter(bitz_volume__gt=MinVolume, coinex_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['bitz_bibox'] = BitzBibox.objects.filter(bitz_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                         profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['huobi_coinex'] = HuobiCoinex.objects.filter(huobi_volume__gt=MinVolume, coinex_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['huobi_bibox'] = HuobiBibox.objects.filter(huobi_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                           profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        filters['coinex_bibox'] = CoinexBibox.objects.filter(coinex_volume__gt=MinVolume, bibox_volume__gt=MinVolume,
                                                             profit__gt=MinProfit, profit__lt=MaxProfit).order_by(
            'name').order_by('-profit')
        serializer = ArbitrageSerializers(filters)
        return Response(serializer.data)


class ExchangeView(APIView):
    """ ВЫВОД ДАННЫХ ОДНОЙ УКАЗАННОЙ БИРЖИ """
    permission_classes = (IsAuthenticated,)
    exchange = {'Binance': {'model': Binance, 'serializer': BinanceSerializer},
                'Bittrex': {'model': Bittrex, 'serializer': BittrexSerializer},
                'Poloniex': {'model': Poloniex, 'serializer': PoloniexSerializer},
                'HitBTC': {'model': Hitbtc, 'serializer': HitbtcSerializer},
                'Livecoin': {'model': Livecoin, 'serializer': LivecoinSerializer},
                'Kucoin': {'model': Kucoin, 'serializer': KucoinSerializer},
                'Kraken': {'model': Kraken, 'serializer': KrakenSerializer},
                'Huobi': {'model': Huobi, 'serializer': HuobiSerializer},
                'OKex': {'model': Okex, 'serializer': OkexSerializer},
                'Gate.io': {'model': Gateio, 'serializer': GateioSerializer},
                'Coinex': {'model': Coinex, 'serializer': CoinexSerializer},
                'Bit-Z': {'model': Bitz, 'serializer': BitzSerializer},
                'Bibox': {'model': Bibox, 'serializer': BiboxSerializer}}

    def get_object(self, slug):
        return self.exchange[slug]['model'].objects.all().order_by('name')

    def get(self, request, slug):
        queryset = self.get_object(slug)
        serializer = self.exchange[slug]['serializer'](queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class TradingView(APIView):
    """ ВЫВОД СПИСКА ТОРГУЕМЫХ МОНЕТ """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        trading = Trading.objects.filter(user=request.data)
        serializer = TradingSerializer(trading, many=True)
        return Response(serializer.data)


class TradingChangeView(APIView):
    """ ВНЕСЕНИЕ ИЗМЕНЕНИЙ В СПИСОК ТОРГУЕМЫХ МОНЕТ """
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        return Trading.objects.get(pk=pk)

    def patch(self, request, pk):
        queryset = self.get_object(pk)
        serializer = TradingSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TradingAddView(generics.CreateAPIView):
    """ ДОБАВЛЕНИЕ МОНЕТЫ В СПИСОК ТОГРУЕМЫХ МОНЕТ """
    permission_classes = (IsAuthenticated,)

    serializer_class = TradingSerializer
    queryset = Trading.objects.all()


class TrackingView(APIView):
    """ СПИСОК МОНЕТ ДЛЯ ОТСЛЕЖИВАНИЯ ИЗМЕНЕНИЯ ПОКАЗАТЕЛЕЙ МОНЕТЫ """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tracking = Tracking.objects.filter(user=request.data)
        serializer = TrackingSerializer(tracking, many=True)
        return Response(serializer.data)


class TrackingChangeView(APIView):
    """ ИЗМЕНЕНИЕ СПИСКА ОТСЛЕЖИВАЕМЫХ МОНЕТ """
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        return Tracking.objects.get(pk=pk)

    def patch(self, request, pk):
        queryset = self.get_object(pk)
        serializer = TrackingSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrackingAddView(generics.CreateAPIView):
    """ ДОБАВЛЕНИЕ В СПИСОК ОТСЛЕЖИВАЕМЫХ МОНЕТ """
    permission_classes = (IsAuthenticated,)

    serializer_class = TrackingSerializer
    queryset = Trading.objects.all()
