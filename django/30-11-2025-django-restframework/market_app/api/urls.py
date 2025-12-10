from django.urls import path
from .views import MarketsView, SellersView, MarketSingleView, market_single_view, seller_view, product_view, product_single_view, seller_single_view

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketSingleView.as_view()),
    path('seller/', SellersView.as_view()),
    path('seller/<int:pk>/', seller_single_view, name='single_seller'),
    path('product/', product_view),
    path('product/<int:pk>', product_single_view),
]
