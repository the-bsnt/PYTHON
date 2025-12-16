from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, mixins
from .models import Products
from .serializers import ProductSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache


class ProductListCreateAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    @method_decorator(cache_page(60 * 15, key_prefix="product_list"))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        import time

        time.sleep(2)
        return super().get_queryset()


def clear_cache(request):
    cache.clear()
    return HttpResponse("Cache cleared")
