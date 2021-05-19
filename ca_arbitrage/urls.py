"""

    ca_backend URL Configuration

"""

from django.urls import path
from ca_arbitrage.views import ArbitrageView, BalanceView, ListingView, ExchangesView, ExchangeView, GraphView, \
    TradingView, TradingChangeView, TradingAddView, TrackingView, TrackingAddView, TrackingChangeView, UserView, \
    UserAccountView, UsersPaymentsView, PricesView, PayView
from .Server import update_balance, update_tracking, update_trading, update_arbitrage

urlpatterns = [
    path('arbitrage', ArbitrageView.as_view()),
    path('balance', BalanceView.as_view()),
    path('listing', ListingView.as_view()),
    path('exchange', ExchangesView.as_view()),
    path('exchange/<slug>', ExchangeView.as_view()),
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
