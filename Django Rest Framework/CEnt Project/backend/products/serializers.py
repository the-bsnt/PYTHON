from rest_framework import serializers
from .models import *
from rest_framework.reverse import reverse
from .validators import *
from api.serializers import *


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    related_products = ProductInlineSerializer(
        source="user.product_set.all", read_only=True, many=True
    )
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="product-edit", lookup_field="pk"
    )
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title, title_no_hello])
    name = serializers.CharField(source="title", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "url",
            "owner",  # user_id
            "edit_url",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
            "email",
            "name",
            "related_products",
        ]

    # & custom validation with serializer    def validate_<fieldname> (self,value):
    # def validate_title(self, value):
    #     request = self.context.get("request")
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             f"{value} is already exists as product name"
    #         )
    #     return value

    # & create and update methods in model serializer
    def create(self, validated_data):
        email = validated_data.pop("email")
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        email = validated_data.pop("email")
        return super().update(instance, validated_data)

    def get_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
