"""ca_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ca_arbitrage import views
from ca_arbitrage.views import ArbitrageView, BalanceView, ListingView, ExchangesView, ExchangeView, GraphView, \
    TradingView, TradingChangeView, TradingAddView, TrackingView, TrackingAddView, TrackingChangeView

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
]
