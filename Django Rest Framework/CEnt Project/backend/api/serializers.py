from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )


class ProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    # id = serializers.IntegerField(read_only=True)
    # email = serializers.EmailField(sread_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        request = self.context.get("request")
        my_products_qs = obj.product_set.all()
        return UserProductInlineSerializer(
            my_products_qs, many=True, context=self.context
        ).data


# & to retrive all user details
# from django.contrib.auth.models import User  # or your custom User model


# class UserPublicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
