from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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
    
    
    # general view override 
    # due to login/auth check
    def create(self, request, *args, **kwargs):
        #로그인된 사용자일 경우에만
        
        if request.META["HTTP_X_USERNAME"] != 'anonymousUser':
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=200)
        else:
            return Response("NO USER")


    def patch(self, request, *args, **kwargs):
        # 나 == 글작성자
        username = request.META["HTTP_X_USERNAME"]
        writer = request.data["writer"]
        product_no = request.data["product_no"]
        if username == writer:
            kwargs['partial'] = True
            partial = kwargs.pop('partial', False)
            instance = get_object_or_404(ProductInfo, pk=product_no)
            serializer = self.serializer_class(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=200)
        else:
            return Response("WRONG USER")


    def delete(self, request, *args, **kwargs):
        username = request.META["HTTP_X_USERNAME"]
        writer = request.data["writer"]
        pk = request.data["product_no"]
        if username == writer:
            instance = get_object_or_404(ProductInfo, pk=pk)
            instance.delete()
            return Response(status=204)
        else:
            return Response("NO AUTHORIZATION")
        
    
    @action(detail=False)
    def search(self, request):
        main_category_no = request.GET.get('main_category', None)
        sub_category_no = request.GET.get('sub_category', None)
        content = request.GET.get('content', None)

        products = self.queryset
        # 카테고리 필터링
        if main_category_no:
            products = products.filter(main_category_no=main_category_no)
            if sub_category_no:
                products = products.filter(sub_category_no=sub_category_no)
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
    def sold(self, request, pk):
        # 요청 보내는 사람과 판매글 작성자가 같은지 확인
        
        username = request.META["HTTP_X_USERNAME"]

        buyer = request.data["buyer"]
        product = self.queryset.get(pk=pk)
        seller = product.writer
        status = product.status

        if username == seller:
            if status == 1: #팔 -> 안팔
                product_serializer = ProductSerializer(product, data={"status": 0}, partial=True)

                purchase_detail = PurchaseDetails.objects.get(product_no=pk)
                purchase_detail.delete()

            else: # 안팔 -> 팔
                product_serializer = ProductSerializer(product, data={"status": 1}, partial=True)
                purchase_serializer = PurchaseDetailsSerializer(data={"seller": seller, "buyer": buyer, "product_no": pk})
                if purchase_serializer.is_valid():
                    purchase_serializer.save()
                else:
                    return HTTPResponse("형식 또는 입력이 옳지 않습니다.")

            if product_serializer.is_valid():
                product_serializer.save()

                return HTTPResponse(status=200)
        
        return HTTPResponse("본인의 판매글만 변경할 수 있습니다.")



    @action(detail=False)
    def categories(self, request):
        main_categories = MainCategoryInfo.objects.all()
        sub_categories = SubCategoryInfo.objects.all()

        total_categories = dict()

        for main_cat in main_categories:
            total_categories[main_cat.main_category_name] = []

        for sub_cat in sub_categories:
            total_categories[sub_cat.main_category_no.main_category_name].append(sub_cat.sub_category_name)

        return Response(total_categories)
        
        



    

    

