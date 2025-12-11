from rest_framework import serializers
from market_app.models import Market, Seller, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MarketSerializer(serializers.ModelSerializer):

    sellers = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='seller-detail')

    class Meta:
        model = Market
        fields = '__all__'


class SellerDetailSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets'
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = ['id', 'name', 'market_count',
                  'market_ids', 'markets', 'contact_info']

    def get_market_count(self, obj):
        return obj.markets.count()


class SellerListSerializer(SellerDetailSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name', 'market_count',
                  'market_ids', 'contact_info']


class ProductDetailSerializer(serializers.ModelSerializer):
    market = MarketSerializer(read_only=True)
    market_id = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        write_only=True,
        source='market'
    )
    seller = SellerDetailSerializer(read_only=True)
    seller_id = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        write_only=True,
        source='seller'
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'market_id', 'market', 'seller', 'seller_id']
