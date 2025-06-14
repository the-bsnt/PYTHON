from django.urls import path
from .views import *

urlpatterns = [
    path("users/", get_user, name="get_user"),
]
