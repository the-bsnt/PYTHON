from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, mixins
from .models import Products
from .serializers import ProductSerializer


class ProductListCreateAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
