from django.urls import path

from .views import *


# URLConf module
urlpatterns = [
    path("", room, name="room"),
    path("<str:id>/", room_detail, name="room_detail"),
]
