from django.urls import path
from .views import *


app_name = "myapp2"
urlpatterns = [
    path("", index, name="index"),
]
