from rest_framework import serializers

from .models import ProductInfo, MainCategoryInfo, SubCategoryInfo, PurchaseDetails, ViewDetails, MainCategoryInfo, MediumCategoryInfo, SubCategoryInfo, User

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

class ProductDetailSerializer(serializers.ModelSerializer):
    main_category_name = serializers.SerializerMethodField('get_main_category_name')
    medium_category_name = serializers.SerializerMethodField('get_medium_category_name')
    sub_category_name = serializers.SerializerMethodField('get_sub_category_name')
    
    class Meta:
        model = ProductInfo
        fields = ["no", "writer", "title", "content", "contact", "price", "photo", "eco_point", "main_category_no", "medium_category_no", "sub_category_no", "status", "reg_time","main_category_name", "medium_category_name", "sub_category_name"]

    def get_main_category_name(self, product):
        return product.main_category_no.main_category_name
    
    def get_medium_category_name(self, product):
        return product.medium_category_no.medium_category_name

    def get_sub_category_name(self, product):
        return product.sub_category_no.sub_category_name


class MainCategoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategoryInfo
        fields = "__all__"
        read_only_fields = (["no"])

class MediumCategoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediumCategoryInfo
        fields = "__all__"
        read_only_fields = (["no"])

class SubCategoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryInfo
        fields = "__all__"
        read_only_fields = (["no"])


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'gender', 'age']
        read_only_fields = (['no'])
