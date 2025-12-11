from django.urls import path, include
from .views import MarketsView, SellersView, MarketSingleView, SellerOfMarketList, ProductViewSet, product_view, product_single_view, seller_single_view
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketSingleView.as_view()),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', SellersView.as_view()),
    path('seller/<int:pk>/', seller_single_view, name='seller-detail'),
    # path('product/', product_view),
    # path('product/<int:pk>', product_single_view),
]
