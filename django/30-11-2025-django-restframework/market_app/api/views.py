from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer, SellerDetailSerializer, ProductDetailSerializer
from market_app.models import Market, Seller, Product
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class MarketsView(generics.ListCreateAPIView):

    ## Mixin class view ##
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

## get and post are already summarized inside of generics.ListCreateAPIView ##
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

## Normal class view ##
    # def get(self, request):
    #     markets = Market.objects.all()
    #     serializer = MarketSerializer(
    #         markets, many=True, context={'request': request})
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = MarketSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def markets_view(request):

    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = MarketSerializer(
            markets, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MarketSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

# class MarketSingleView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Market.objects.all()
#     serializer_class = MarketSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


@api_view(['GET', 'DELETE', 'PUT'])
def market_single_view(request, pk):

    if request.method == 'GET':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market, context={'request': request})
        return Response(serializer.data)

    if request.method == 'DELETE':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market)
        market.delete()
        return Response(serializer.data)

    if request.method == 'PUT':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(
            market, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


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


@api_view(['GET', 'POST'])
def seller_view(request):

    if request.method == 'GET':
        sellers = Seller.objects.all()
        serializer = SellerDetailSerializer(
            sellers, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SellerDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


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
