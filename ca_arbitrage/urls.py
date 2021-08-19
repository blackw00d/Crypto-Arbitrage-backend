"""

    ca_backend URL Configuration

"""

from django.views.decorators.cache import cache_page
from django.urls import path
from ca_backend.settings import TIMEOUT
from ca_arbitrage.views import ArbitrageView, BalanceView, ListingView, ExchangesView, ExchangeView, GraphView, \
    TradingView, TradingChangeView, TradingAddView, TrackingView, TrackingAddView, TrackingChangeView, UserView, \
    UserAccountView, UsersPaymentsView, PricesView, PayView
from .Server import update_balance, update_tracking, update_trading, update_arbitrage

urlpatterns = [
    path('arbitrage', cache_page(TIMEOUT)(ArbitrageView.as_view())),
    path('balance', cache_page(TIMEOUT)(BalanceView.as_view())),
    path('listing', cache_page(TIMEOUT)(ListingView.as_view())),
    path('exchange', cache_page(TIMEOUT)(ExchangesView.as_view())),
    path('exchange/<slug>', cache_page(TIMEOUT)(ExchangeView.as_view())),
    path('graph/<slug>', GraphView.as_view()),
    path('trading', TradingView.as_view()),
    path('trading/add', TradingAddView.as_view()),
    path('trading/change/<int:pk>', TradingChangeView.as_view()),
    path('tracking', TrackingView.as_view()),
    path('tracking/add', TrackingAddView.as_view()),
    path('tracking/change/<int:pk>', TrackingChangeView.as_view()),
    path('user', UserView.as_view()),
    path('account', UserAccountView.as_view()),
    path('payments', UsersPaymentsView.as_view()),
    path('prices', PricesView.as_view()),
    path('pay', PayView.as_view()),

    path('update_balance', update_balance.main),
    path('update_tracking', update_tracking.main),
    path('update_trading', update_trading.main),
    path('update_arbitrage', update_arbitrage.main)
]
