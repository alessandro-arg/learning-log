from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer, SellerDetailSerializer, ProductDetailSerializer, SellerListSerializer
from market_app.models import Market, Seller, Product
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class MarketsView(generics.ListCreateAPIView):

    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class MarketSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class SellerOfMarketList(generics.ListCreateAPIView):
    serializer_class = SellerListSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        market = Market.objects.get(pk=pk)
        return market.sellers.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        market = Market.objects.get(pk=pk)
        serializer.save(markets=[market])


@api_view(['GET'])
def seller_single_view(request, pk):
    if request.method == 'GET':
        seller = Seller.objects.get(pk=pk)
        serializer = SellerDetailSerializer(
            seller, context={'request': request})
        return Response(serializer.data)


class SellersView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Seller.objects.all()
    serializer_class = SellerDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view(['GET'])
def product_single_view(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        serializer = ProductDetailSerializer(
            product, context={'request': request})
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_view(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductDetailSerializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductDetailSerializer(product).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
