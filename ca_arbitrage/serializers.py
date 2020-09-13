from rest_framework import serializers
from .models import *


class BinanceBittrexSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceBittrex
        exclude = ["id"]


class BinanceHitbtcSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceHitbtc
        exclude = ["id"]


class BinanceKucoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceKucoin
        exclude = ["id"]


class BinanceLivecoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceLivecoin
        exclude = ["id"]


class BinancePoloniexSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinancePoloniex
        exclude = ["id"]


class BinanceKrakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceKraken
        exclude = ["id"]


class BinanceOkexSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceOkex
        exclude = ["id"]


class BinanceGateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceGateio
        exclude = ["id"]


class BinanceBitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceBitz
        exclude = ["id"]


class BinanceHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceHuobi
        exclude = ["id"]


class BinanceCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceCoinex
        exclude = ["id"]


class BinanceBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceBibox
        exclude = ["id"]


class BittrexHitbtcSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexHitbtc
        exclude = ["id"]


class BittrexKucoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexKucoin
        exclude = ["id"]


class BittrexLivecoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexLivecoin
        exclude = ["id"]


class BittrexPoloniexSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexPoloniex
        exclude = ["id"]


class BittrexKrakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexKraken
        exclude = ["id"]


class BittrexOkexSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexOkex
        exclude = ["id"]


class BittrexGateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexGateio
        exclude = ["id"]


class BittrexBitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexBitz
        exclude = ["id"]


class BittrexHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexHuobi
        exclude = ["id"]


class BittrexCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexCoinex
        exclude = ["id"]


class BittrexBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = BittrexBibox
        exclude = ["id"]


class PoloniexHitbtcSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexHitbtc
        exclude = ["id"]


class PoloniexKucoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexKucoin
        exclude = ["id"]


class PoloniexLivecoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexLivecoin
        exclude = ["id"]


class PoloniexKrakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexKraken
        exclude = ["id"]


class PoloniexOkexSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexOkex
        exclude = ["id"]


class PoloniexGateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexGateio
        exclude = ["id"]


class PoloniexBitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexBitz
        exclude = ["id"]


class PoloniexHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexHuobi
        exclude = ["id"]


class PoloniexCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexCoinex
        exclude = ["id"]


class PoloniexBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloniexBibox
        exclude = ["id"]


class HitbtcKucoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitbtcKucoin
        exclude = ["id"]


class HitbtcLivecoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitbtcLivecoin
        exclude = ["id"]


class HitbtckrakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hitbtckraken
        exclude = ["id"]


class HitbtcOkexSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitbtcOkex
        exclude = ["id"]


class HitbtcGateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitbtcGateio
        exclude = ["id"]


class HitbtcBitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitbtcBitz
        exclude = ["id"]


class HitbtcHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitbtcHuobi
        exclude = ["id"]


class HitbtcCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitbtcCoinex
        exclude = ["id"]


class HitbtcBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitbtcBibox
        exclude = ["id"]


class KucoinLivecoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = KucoinLivecoin
        exclude = ["id"]


class KucoinKrakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KucoinKraken
        exclude = ["id"]


class KucoinOkexSerializer(serializers.ModelSerializer):
    class Meta:
        model = KucoinOkex
        exclude = ["id"]


class KucoinGateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = KucoinGateio
        exclude = ["id"]


class KucoinBitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = KucoinBitz
        exclude = ["id"]


class KucoinHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = KucoinHuobi
        exclude = ["id"]


class KucoinCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = KucoinCoinex
        exclude = ["id"]


class KucoinBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = KucoinBibox
        exclude = ["id"]


class LivecoinKrakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivecoinKraken
        exclude = ["id"]


class LivecoinOkexSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivecoinOkex
        exclude = ["id"]


class LivecoinGateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivecoinGateio
        exclude = ["id"]


class LivecoinBitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivecoinBitz
        exclude = ["id"]


class LivecoinHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivecoinHuobi
        exclude = ["id"]


class LivecoinCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivecoinCoinex
        exclude = ["id"]


class LivecoinBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivecoinBibox
        exclude = ["id"]


class KrakenOkexSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrakenOkex
        exclude = ["id"]


class KrakenGateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrakenGateio
        exclude = ["id"]


class KrakenBitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrakenBitz
        exclude = ["id"]


class KrakenHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrakenHuobi
        exclude = ["id"]


class KrakenCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrakenCoinex
        exclude = ["id"]


class KrakenBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrakenBibox
        exclude = ["id"]


class OkexGateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = OkexGateio
        exclude = ["id"]


class OkexBitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = OkexBitz
        exclude = ["id"]


class OkexHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = OkexHuobi
        exclude = ["id"]


class OkexCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = OkexCoinex
        exclude = ["id"]


class OkexBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = OkexBibox
        exclude = ["id"]


class GateioBitzSerializer(serializers.ModelSerializer):
    class Meta:
        model = GateioBitz
        exclude = ["id"]


class GateioHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = GateioHuobi
        exclude = ["id"]


class GateioCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = GateioCoinex
        exclude = ["id"]


class GateioBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = GateioBibox
        exclude = ["id"]


class BitzHuobiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitzHuobi
        exclude = ["id"]


class BitzCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitzCoinex
        exclude = ["id"]


class BitzBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitzBibox
        exclude = ["id"]


class HuobiCoinexSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuobiCoinex
        exclude = ["id"]


class HuobiBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuobiBibox
        exclude = ["id"]


class CoinexBiboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinexBibox
        exclude = ["id"]


class FiltersSerializers(serializers.Serializer):
    BinanceBittrex = BinanceBittrexSerializer(many=True)
    BinanceHitbtc = BinanceHitbtcSerializer(many=True)
    BinanceKucoin = BinanceKucoinSerializer(many=True)
    BinancePoloniex = BinancePoloniexSerializer(many=True)
    BinanceKraken = BinanceKrakenSerializer(many=True)
    BinanceOkex = BinanceOkexSerializer(many=True)
    BinanceGateio = BinanceGateioSerializer(many=True)
    BinanceBitz = BinanceBitzSerializer(many=True)
    BinanceHuobi = BinanceHuobiSerializer(many=True)
    BinanceCoinex = BinanceCoinexSerializer(many=True)
    BinanceBibox = BinanceBiboxSerializer(many=True)
    BittrexHitbtc = BittrexHitbtcSerializer(many=True)
    BittrexKucoin = BittrexKucoinSerializer(many=True)
    BittrexLivecoin = BittrexLivecoinSerializer(many=True)
    BittrexPoloniex = BittrexPoloniexSerializer(many=True)
    BittrexKraken = BittrexKrakenSerializer(many=True)
    BittrexOkex = BittrexOkexSerializer(many=True)
    BittrexGateio = BittrexGateioSerializer(many=True)
    BittrexBitz = BittrexBitzSerializer(many=True)
    BittrexHuobi = BittrexHuobiSerializer(many=True)
    BittrexCoinex = BittrexCoinexSerializer(many=True)
    BittrexBibox = BittrexBiboxSerializer(many=True)
    PoloniexHitbtc = PoloniexHitbtcSerializer(many=True)
    PoloniexKucoin = PoloniexKucoinSerializer(many=True)
    PoloniexLivecoin = PoloniexLivecoinSerializer(many=True)
    PoloniexKraken = PoloniexKrakenSerializer(many=True)
    PoloniexOkex = PoloniexOkexSerializer(many=True)
    PoloniexGateio = PoloniexGateioSerializer(many=True)
    PoloniexBitz = PoloniexBitzSerializer(many=True)
    PoloniexHuobi = PoloniexHuobiSerializer(many=True)
    PoloniexCoinex = PoloniexCoinexSerializer(many=True)
    PoloniexBibox = PoloniexBiboxSerializer(many=True)
    HitbtcKucoin = HitbtcKucoinSerializer(many=True)
    HitbtcLivecoin = HitbtcLivecoinSerializer(many=True)
    Hitbtckraken = HitbtckrakenSerializer(many=True)
    HitbtcOkex = HitbtcOkexSerializer(many=True)
    HitbtcGateio = HitbtcGateioSerializer(many=True)
    HitbtcBitz = HitbtcBitzSerializer(many=True)
    HitbtcHuobi = HitbtcHuobiSerializer(many=True)
    HitbtcCoinex = HitbtcCoinexSerializer(many=True)
    HitbtcBibox = HitbtcBiboxSerializer(many=True)
    KucoinLivecoin = KucoinLivecoinSerializer(many=True)
    KucoinKraken = KucoinKrakenSerializer(many=True)
    KucoinOkex = KucoinOkexSerializer(many=True)
    KucoinGateio = KucoinGateioSerializer(many=True)
    KucoinBitz = KucoinBitzSerializer(many=True)
    KucoinHuobi = KucoinHuobiSerializer(many=True)
    KucoinCoinex = KucoinCoinexSerializer(many=True)
    KucoinBibox = KucoinBiboxSerializer(many=True)
    LivecoinKraken = LivecoinKrakenSerializer(many=True)
    LivecoinOkex = LivecoinOkexSerializer(many=True)
    LivecoinGateio = LivecoinGateioSerializer(many=True)
    LivecoinBitz = LivecoinBitzSerializer(many=True)
    LivecoinHuobi = LivecoinHuobiSerializer(many=True)
    LivecoinCoinex = LivecoinCoinexSerializer(many=True)
    LivecoinBibox = LivecoinBiboxSerializer(many=True)
    KrakenOkex = KrakenOkexSerializer(many=True)
    KrakenGateio = KrakenGateioSerializer(many=True)
    KrakenBitz = KrakenBitzSerializer(many=True)
    KrakenHuobi = KrakenHuobiSerializer(many=True)
    KrakenCoinex = KrakenCoinexSerializer(many=True)
    KrakenBibox = KrakenBiboxSerializer(many=True)
    OkexGateio = OkexGateioSerializer(many=True)
    OkexBitz = OkexBitzSerializer(many=True)
    OkexHuobi = OkexHuobiSerializer(many=True)
    OkexCoinex = OkexCoinexSerializer(many=True)
    OkexBibox = OkexBiboxSerializer(many=True)
    GateioBitz = GateioBitzSerializer(many=True)
    GateioHuobi = GateioHuobiSerializer(many=True)
    GateioCoinex = GateioCoinexSerializer(many=True)
    GateioBibox = GateioBiboxSerializer(many=True)
    BitzHuobi = BitzHuobiSerializer(many=True)
    BitzCoinex = BitzCoinexSerializer(many=True)
    BitzBibox = BitzBiboxSerializer(many=True)
    HuobiCoinex = HuobiCoinexSerializer(many=True)
    HuobiBibox = HuobiBiboxSerializer(many=True)
    CoinexBibox = CoinexBiboxSerializer(many=True)
