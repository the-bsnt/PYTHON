from django.urls import path
from .views import *

# URL CONF
urlpatterns = [path("", polls, name="polls")]
