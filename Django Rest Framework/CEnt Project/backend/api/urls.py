from django.urls import path

from .views import *

app_name = "api"
urlpatterns = [
    path("", api_home, name="api_home"),
]
