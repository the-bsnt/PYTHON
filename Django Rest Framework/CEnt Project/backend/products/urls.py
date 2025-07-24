from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductListCreateAPIView.as_view(), name="product-list"),
    # path("<int:pk>/", product_alt_view),
    path("<int:pk>/", ProductMixinView.as_view(), name="product-detail"),
    path("<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product-edit"),
    path("<int:pk>/delete/", ProductDeleteAPIView.as_view()),
]
