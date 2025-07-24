from django.shortcuts import render
from rest_framework import generics, mixins, permissions, authentication
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from api.permission import *
from api.authentication import *
from api.mixins import *


# & GENERIC API VIEW
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(
    UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # permission_classes = [IsStaffEditorPermission]

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)  # send a Django signal

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=user)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UserQuerySetMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

        # return super().perform_update(serializer)


class ProductDeleteAPIView(UserQuerySetMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# & Using FUNCTION BASED VIEWS for Create Retrieve or List


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            # instance = Product.objects.get(pk=pk)
            instance = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(instance).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or title

            serializer.save(content=content)
            return Response(serializer.data)


# & MIXINS AND GENERIC API VIEW
class ProductMixinView(
    UserQuerySetMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffEditorPermission]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
