from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ProductInfo, MainCategoryInfo, SubCategoryInfo, PurchaseDetails
from .serializers import ProductSerializer, PurchaseDetailsSerializer


# Create your views here.

# The actions provided by the ModelViewSet class are 
# .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductInfo.objects.order_by("-pk")
    serializer_class = ProductSerializer
    
    @action(detail=False)
    def search(self, request):
        category = request.GET.get('category', None)
        content = request.GET.get('content', None)

        products = self.queryset
        # 카테고리 필터링
        if category:
            products = products.filter(main_category_no=category)
        # 검색어 필터링
        if content:
            products = products.filter(title__icontains=content)

        serializer = self.serializer_class(products, many=True)

        return Response(serializer.data)

    
    @action(detail=False)
    def recommendation(self, request):
        # 상품 추천 로직

        # 추천 상품 목록 리턴

        pass
    
    @action(detail=True)
    def sold(self, request):
        # 요청 보내는 사람과 판매글 작성자가 같은지 확인
        # 토큰  값
        # request.META["HTTP_AUTHORIZATION"]
        # request.META.get("Authorization")
        
        user_id = request.META["user_id"]
        product_no = request.data["product_no"]
        buyer = request.data["buyer"]

        product = self.queryset.get(pk=product_no)
        seller = product.writer
        status = product.status

        if user_id == seller:
            if status == 1: #팔 -> 안팔
                product_serializer = ProductSerializer(product, data={"status": 0}, partial=True)

                purchase_detail = PurchaseDetails.objects.get(product_no=product_no)
                purchase_detail.delete()

            else: # 안팔 -> 팔
                product_serializer = ProductSerializer(product, data={"status": 1}, partial=True)
                purchase_serializer = PurchaseDetailsSerializer(data={"seller": seller, "buyer": buyer, "product_no": product_no})
                if purchase_serializer.is_valid():
                    purchase_serializer.save()
                else:
                    return HTTPResponse("형식 또는 입력이 옳지 않습니다.")

            if product_serializer.is_valid():
                product_serializer.save()

                return HTTPResponse(status=200)
        
        return HTTPResponse("본인의 판매글만 변경할 수 있습니다.")



    @action(detail=True)
    def categories(self, request):
        main_categories = MainCategoryInfo.objects.all()
        sub_categories = SubCategoryInfo.objects.all()

        total_categories = dict()

        for main_cat in main_categories:
            total_categories[main_cat.main_category_name] = []

        for sub_cat in sub_categories:
            if sub_cat.main_category_no == main_cat.no:
                total_categories[main_cat.main_category_name].append(sub_cat.sub_category_name)

        return Response(total_categories)
        
        



    

    

