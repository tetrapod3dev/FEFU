from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ProductInfo, MainCategoryInfo, SubCategoryInfo
from .serializers import ProductSerializer


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
        
        

        pass

    @action(detail=True)
    def categories(self, request):
        main_category = MainCategoryInfo.objects.all()
        sub_category = SubCategoryInfo.objects.all()
        
        #적절한 형태로 변환해서 return



    

    

