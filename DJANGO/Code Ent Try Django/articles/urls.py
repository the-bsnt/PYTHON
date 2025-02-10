from django.urls import path
from .views import *

urlpatterns = [path("", article_home), path("search/", article_search_view)]
