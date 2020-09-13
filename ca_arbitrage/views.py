from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


def list_todo_items(request):
    list = BinanceBittrex.objects.all()
    return render(request, 'ca_arbitrage/index.html', {'items': list})


class FiltersView(APIView):
    def get(self, request):
        filters = {}
        MinVolume = 30000
        MinProfit = 0.01
        MaxProfit = 100
        filters['BinanceBittrex'] = BinanceBittrex.objects.filter(binance_volume__gt=MinVolume, bittrex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinanceHitbtc'] = BinanceHitbtc.objects.filter(binance_volume__gt=MinVolume, hitbtc_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinanceKucoin'] = BinanceKucoin.objects.filter(binance_volume__gt=MinVolume, kucoin_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinancePoloniex'] = BinancePoloniex.objects.filter(binance_volume__gt=MinVolume, poloniex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinanceKraken'] = BinanceKraken.objects.filter(binance_volume__gt=MinVolume, kraken_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinanceOkex'] = BinanceOkex.objects.filter(binance_volume__gt=MinVolume, okex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinanceGateio'] = BinanceGateio.objects.filter(binance_volume__gt=MinVolume, gateio_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinanceBitz'] = BinanceBitz.objects.filter(binance_volume__gt=MinVolume, bitz_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinanceHuobi'] = BinanceHuobi.objects.filter(binance_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinanceCoinex'] = BinanceCoinex.objects.filter(binance_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BinanceBibox'] = BinanceBibox.objects.filter(binance_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexHitbtc'] = BittrexHitbtc.objects.filter(bittrex_volume__gt=MinVolume, hitbtc_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexKucoin'] = BittrexKucoin.objects.filter(bittrex_volume__gt=MinVolume, kucoin_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexLivecoin'] = BittrexLivecoin.objects.filter(bittrex_volume__gt=MinVolume, livecoin_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexPoloniex'] = BittrexPoloniex.objects.filter(bittrex_volume__gt=MinVolume, poloniex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexKraken'] = BittrexKraken.objects.filter(bittrex_volume__gt=MinVolume, kraken_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexOkex'] = BittrexOkex.objects.filter(bittrex_volume__gt=MinVolume, okex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexGateio'] = BittrexGateio.objects.filter(bittrex_volume__gt=MinVolume, gateio_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexBitz'] = BittrexBitz.objects.filter(bittrex_volume__gt=MinVolume, bitz_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexHuobi'] = BittrexHuobi.objects.filter(bittrex_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexCoinex'] = BittrexCoinex.objects.filter(bittrex_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BittrexBibox'] = BittrexBibox.objects.filter(bittrex_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexHitbtc'] = PoloniexHitbtc.objects.filter(poloniex_volume__gt=MinVolume, hitbtc_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexKucoin'] = PoloniexKucoin.objects.filter(poloniex_volume__gt=MinVolume, kucoin_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexLivecoin'] = PoloniexLivecoin.objects.filter(poloniex_volume__gt=MinVolume, livecoin_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexKraken'] = PoloniexKraken.objects.filter(poloniex_volume__gt=MinVolume, kraken_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexOkex'] = PoloniexOkex.objects.filter(poloniex_volume__gt=MinVolume, okex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexGateio'] = PoloniexGateio.objects.filter(poloniex_volume__gt=MinVolume, gateio_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexBitz'] = PoloniexBitz.objects.filter(poloniex_volume__gt=MinVolume, bitz_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexHuobi'] = PoloniexHuobi.objects.filter(poloniex_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexCoinex'] = PoloniexCoinex.objects.filter(poloniex_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['PoloniexBibox'] = PoloniexBibox.objects.filter(poloniex_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HitbtcKucoin'] = HitbtcKucoin.objects.filter(hitbtc_volume__gt=MinVolume, kucoin_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HitbtcLivecoin'] = HitbtcLivecoin.objects.filter(hitbtc_volume__gt=MinVolume, livecoin_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['Hitbtckraken'] = Hitbtckraken.objects.filter(hitbtc_volume__gt=MinVolume, kraken_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HitbtcOkex'] = HitbtcOkex.objects.filter(hitbtc_volume__gt=MinVolume, okex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HitbtcGateio'] = HitbtcGateio.objects.filter(hitbtc_volume__gt=MinVolume, gateio_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HitbtcBitz'] = HitbtcBitz.objects.filter(hitbtc_volume__gt=MinVolume, bitz_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HitbtcHuobi'] = HitbtcHuobi.objects.filter(hitbtc_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HitbtcCoinex'] = HitbtcCoinex.objects.filter(hitbtc_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HitbtcBibox'] = HitbtcBibox.objects.filter(hitbtc_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KucoinLivecoin'] = KucoinLivecoin.objects.filter(kucoin_volume__gt=MinVolume, livecoin_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KucoinKraken'] = KucoinKraken.objects.filter(kucoin_volume__gt=MinVolume, kraken_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KucoinOkex'] = KucoinOkex.objects.filter(kucoin_volume__gt=MinVolume, okex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KucoinGateio'] = KucoinGateio.objects.filter(kucoin_volume__gt=MinVolume, gateio_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KucoinBitz'] = KucoinBitz.objects.filter(kucoin_volume__gt=MinVolume, bitz_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KucoinHuobi'] = KucoinHuobi.objects.filter(kucoin_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KucoinCoinex'] = KucoinCoinex.objects.filter(kucoin_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KucoinBibox'] = KucoinBibox.objects.filter(kucoin_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['LivecoinKraken'] = LivecoinKraken.objects.filter(livecoin_volume__gt=MinVolume, kraken_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['LivecoinOkex'] = LivecoinOkex.objects.filter(livecoin_volume__gt=MinVolume, okex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['LivecoinGateio'] = LivecoinGateio.objects.filter(livecoin_volume__gt=MinVolume, gateio_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['LivecoinBitz'] = LivecoinBitz.objects.filter(livecoin_volume__gt=MinVolume, bitz_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['LivecoinHuobi'] = LivecoinHuobi.objects.filter(livecoin_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['LivecoinCoinex'] = LivecoinCoinex.objects.filter(livecoin_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['LivecoinBibox'] = LivecoinBibox.objects.filter(livecoin_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KrakenOkex'] = KrakenOkex.objects.filter(kraken_volume__gt=MinVolume, okex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KrakenGateio'] = KrakenGateio.objects.filter(kraken_volume__gt=MinVolume, gateio_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KrakenBitz'] = KrakenBitz.objects.filter(kraken_volume__gt=MinVolume, bitz_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KrakenHuobi'] = KrakenHuobi.objects.filter(kraken_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KrakenCoinex'] = KrakenCoinex.objects.filter(kraken_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['KrakenBibox'] = KrakenBibox.objects.filter(kraken_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['OkexGateio'] = OkexGateio.objects.filter(okex_volume__gt=MinVolume, gateio_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['OkexBitz'] = OkexBitz.objects.filter(okex_volume__gt=MinVolume, bitz_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['OkexHuobi'] = OkexHuobi.objects.filter(okex_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['OkexCoinex'] = OkexCoinex.objects.filter(okex_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['OkexBibox'] = OkexBibox.objects.filter(okex_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['GateioBitz'] = GateioBitz.objects.filter(gateio_volume__gt=MinVolume, bitz_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['GateioHuobi'] = GateioHuobi.objects.filter(gateio_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['GateioCoinex'] = GateioCoinex.objects.filter(gateio_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['GateioBibox'] = GateioBibox.objects.filter(gateio_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BitzHuobi'] = BitzHuobi.objects.filter(bitz_volume__gt=MinVolume, huobi_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BitzCoinex'] = BitzCoinex.objects.filter(bitz_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['BitzBibox'] = BitzBibox.objects.filter(bitz_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HuobiCoinex'] = HuobiCoinex.objects.filter(huobi_volume__gt=MinVolume, coinex_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['HuobiBibox'] = HuobiBibox.objects.filter(huobi_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        filters['CoinexBibox'] = CoinexBibox.objects.filter(coinex_volume__gt=MinVolume, bibox_volume__gt=MinVolume, profit__gt=MinProfit, profit__lt=MaxProfit).order_by('name').order_by('-profit')
        serializer = FiltersSerializers(filters)
        return Response(serializer.data)


class BinanceBittrexView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        arbitrage = BinanceBittrex.objects.all()
        serializer = BinanceBittrexSerializer(arbitrage, many=True)
        return Response(serializer.data)
