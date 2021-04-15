from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .services import get_user_balance, get_coin_listing, get_exchange_data, get_graph_data, get_arbitrage_data, \
    get_trading_coins, get_tracking_coins, get_user_keys


class BalanceView(APIView):
    """ Отображение баланса пользователя """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response(get_user_balance(request.user))


class ListingView(APIView):
    """ Отображение списка появившихся монет """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(get_coin_listing())


class ExchangesView(APIView):
    """ Отображение данных с бирж """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(get_exchange_data())


class ArbitrageView(APIView):
    """ Отображение данных арбитража о биржах """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(get_arbitrage_data())


class ExchangeView(APIView):
    """ Отображение данных одной биржи """
    permission_classes = (IsAuthenticated,)
    exchange = {'Binance': {'model': Binance, 'serializer': BinanceSerializer},
                'Bittrex': {'model': Bittrex, 'serializer': BittrexSerializer},
                'Poloniex': {'model': Poloniex, 'serializer': PoloniexSerializer},
                'HitBTC': {'model': Hitbtc, 'serializer': HitbtcSerializer},
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


class GraphView(APIView):
    """ Отображение списка торгуемых монет для пользователя """
    permission_classes = (IsAuthenticated,)

    def post(self, request, slug):
        return Response(get_graph_data(slug, request.data))


class TradingView(APIView):
    """ Отображение списка торгуемых монет для пользователя """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response(get_trading_coins(request.data))


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
    """ Отображение списка отслеживаемых монет для пользователя """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response(get_tracking_coins(request.data))


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


class UserView(APIView):
    """ ПОЛУЧЕНИЕ И ИЗМЕНЕНИЕ API КЛЮЧЕЙ ПОЛЬЗОВАТЕЛЯ """
    permission_classes = (IsAuthenticated,)

    def get_object(self, user):
        return UserKeys.objects.get(user=user)

    def patch(self, request):
        queryset = self.get_object(request.data['user'])
        del request.data['user']
        serializer = UserKeysSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        return Response(get_user_keys(request.user))
