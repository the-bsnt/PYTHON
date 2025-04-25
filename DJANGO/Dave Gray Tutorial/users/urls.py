from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path("", login_user, name="login_user"),
    path("register/", register, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout_view/", logout_view, name="logout_view"),
]
