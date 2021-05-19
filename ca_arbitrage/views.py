from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .services import get_user_balance, get_coin_listing, get_exchange_data, get_graph_data, get_arbitrage_data, \
    get_trading_coins, get_tracking_coins, get_user_keys, get_user_account, get_user_payments, set_user_account
from django.conf import settings


class BalanceView(APIView):
    """ ПОЛУЧЕНИЕ БАЛАНСА ПОЛЬЗОВАТЕЛЯ """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response(data=get_user_balance(request.user), status=status.HTTP_200_OK)


class ListingView(APIView):
    """ ПОЛУЧЕНИЕ СПИСКА ДОБАВЛЕННЫХ НА БИРЖИ МОНЕТ """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data=get_coin_listing(), status=status.HTTP_200_OK)


class ExchangesView(APIView):
    """ ПОЛУЧЕНИЕ ДАННЫХ СО ВСЕХ БИРЖ """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data=get_exchange_data(), status=status.HTTP_200_OK)


class ArbitrageView(APIView):
    """ ПОЛУЧЕНИЕ ДАННЫХ АРБИТРАЖА НА БИРЖАХ """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data=get_arbitrage_data(), status=status.HTTP_200_OK)


class ExchangeView(APIView):
    """ ПОЛУЧЕНИЕ ДАННЫХ ОДНОЙ БИРЖИ """
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
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GraphView(APIView):
    """ ПОЛУЧЕНИЕ ГРАФИКА ЦЕНЫ И ОБЪЕМА МОНЕТЫ НА БИРЖЕ """
    permission_classes = (IsAuthenticated,)

    def post(self, request, slug):
        data, status_code = get_graph_data(slug, request.data)
        return Response(data=data, status=status_code)


class TradingView(APIView):
    """ ПОЛУЧЕНИЕ СПИСКА ТОРГУЕМЫХ МОНЕТ ДЛЯ ПОЛЬЗОВАТЕЛЯ """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response(data=get_trading_coins(request.user), status=status.HTTP_200_OK)


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
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TradingAddView(generics.CreateAPIView):
    """ ДОБАВЛЕНИЕ МОНЕТЫ В СПИСОК ТОГРУЕМЫХ МОНЕТ """
    permission_classes = (IsAuthenticated,)

    queryset = Trading.objects.all()
    serializer_class = TradingSerializer

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return self.create(request, *args, **kwargs)


class TrackingView(APIView):
    """ ПОЛУЧЕНИЕ СПИСКА ОТСЛЕЖИВАЕМЫХ МОНЕТ ДЛЯ ПОЛЬЗОВАТЕЛЯ """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response(data=get_tracking_coins(request.user), status=status.HTTP_200_OK)


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
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrackingAddView(generics.CreateAPIView):
    """ ДОБАВЛЕНИЕ В СПИСОК ОТСЛЕЖИВАЕМЫХ МОНЕТ """
    permission_classes = (IsAuthenticated,)

    serializer_class = TrackingSerializer
    queryset = Trading.objects.all()

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return self.create(request, *args, **kwargs)


class UserView(APIView):
    """ ПОЛУЧЕНИЕ И ИЗМЕНЕНИЕ API КЛЮЧЕЙ, TELEGRAM NICKNAME ПОЛЬЗОВАТЕЛЯ """
    permission_classes = (IsAuthenticated,)

    def get_object(self, user):
        return UsersKeys.objects.get(user=user)

    def patch(self, request):
        queryset = self.get_object(request.user)
        serializer = UserKeysSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        return Response(data=get_user_keys(request.user), status=status.HTTP_200_OK)


class UserAccountView(APIView):
    """ ПОЛУЧЕНИЕ ДАННЫХ АККАУНТА ПОЛЬЗОВАТЕЛЯ """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data=get_user_account(request.user), status=status.HTTP_200_OK)


class UsersPaymentsView(APIView):
    """ ПОЛУЧЕНИЕ СПИСКА ТРАНЗАКЦИЙ ПОЛЬЗОВАТЕЛЯ """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data=get_user_payments(request.user), status=status.HTTP_200_OK)


class PricesView(APIView):
    """ ПОЛУЧЕНИЕ ТАРИФОВ ДЛЯ ПОЛЬЗОВАТЕЛЯ """

    def get(self, request):
        price = {
            'try': settings.PAYMENT,
            'begginer': settings.PAYMENT * 2.75,
            'trader': settings.PAYMENT * 5
        }
        return Response(data=price, status=status.HTTP_200_OK)


class PayView(APIView):
    """ ДОБАВЛЕНИЕ ТРАНЗАКЦИИ ПОЛЬЗОВАТЕЛЮ """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = UsersPaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            set_user_account(request.data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
