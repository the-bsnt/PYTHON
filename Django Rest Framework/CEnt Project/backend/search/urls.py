from django.urls import path

from .views import *

urlpatterns = [
    path("", SearchListView.as_view(), name="search"),
    path("algolia/", SearchListViewAlgolia.as_view(), name="search-algolia"),
]
