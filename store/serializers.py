from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product_name")

    class Meta:
        model = Product
        fields = ["id", "name", "description"]
