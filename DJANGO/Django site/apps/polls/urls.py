from django.urls import path
from .views import *

# URL CONF
urlpatterns = [path("", index, name="index")]
