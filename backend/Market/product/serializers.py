from rest_framework import serializers

from .models import ProductInfo, MainCategoryInfo, SubCategoryInfo, PurchaseDetails, ViewDetails

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = "__all__"
        read_only_fields = (["no", "reg_time"])


class PurchaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetails
        fields = "__all__"
        read_only_fields = (["no"])

class ViewDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewDetails
        fields = "__all__"
        read_only_fields = (["no"])

class ProductDetailSerializer(serializers.Serializer):
    main_category_name = serializers.CharField(max_length=45, read_only=True)
    medium_category_name = serializers.CharField(max_length=45, read_only=True)
    sub_category_name = serializers.Charfield(max_length=45, read_only=True)
    class Meta:
        model = ProductInfo
        fields = ["no", "writer", "title", "content", "contact", "price", "photo", "eco_point", "status", "reg_time"]


