from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already exists as product name")
    return value


def title_no_hello(value):
    if "hello world" in value.lower():
        raise serializers.ValidationError("password":"Hellow is not allowed")
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup="iexact")
