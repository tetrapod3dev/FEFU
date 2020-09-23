from rest_framework import serializers

from .models import ProductInfo, MainCategoryInfo, SubCategoryInfo, PurchaseDetails, ViewDetails

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = "__all__"
        read_only_fields = (["no", "reg_time", "writer"])


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





