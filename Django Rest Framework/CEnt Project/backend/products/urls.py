from django.urls import path
from .views import *

urlpatterns = [
    path("", product_alt_view),
    path("<int:pk>/", product_alt_view),
    path("<int:pk>/update", ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", ProductDeleteAPIView.as_view()),
]
