from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import *

app_name = "api"
urlpatterns = [
    path("auth/", obtain_auth_token),
    path("", api_home, name="api_home"),
    path("api_model/", api_model, name="api_model"),
    path("drf_view/", drf_view, name="drf_view"),
    path("post_view/", post_view, name="post_view"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_refresh"),
]
