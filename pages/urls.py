from django.urls import path

from .views import HomeListView, ShopListView
from product.views import ProductDetailView

urlpatterns = [
    path("", HomeListView.as_view(), name='home'),
    path("shop/", ShopListView.as_view(), name='shop'),
    path("shop/<uuid:pk>/", ProductDetailView.as_view(), name='product'),
]
