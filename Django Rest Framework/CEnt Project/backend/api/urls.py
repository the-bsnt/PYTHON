from django.urls import path

from .views import *

app_name = "api"
urlpatterns = [
    path("", api_home, name="api_home"),
    path("api_model/", api_model, name="api_model"),
    path("drf_view/", drf_view, name="drf_view"),
    path("post_view/", post_view, name="post_view"),
]
