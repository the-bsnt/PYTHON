from django.urls import path
from .views import ProductListCreateAPIView, clear_cache

urlpatterns = [
    path("products/", ProductListCreateAPIView.as_view(), name="test"),
    path("clear/", clear_cache, name="clear-cache"),
]
