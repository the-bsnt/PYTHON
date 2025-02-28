from django.urls import path
from .views import *

# URL CONF
app_name = "polls"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
]
