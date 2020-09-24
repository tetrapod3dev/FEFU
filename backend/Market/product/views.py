from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .models import User, ProductInfo, MainCategoryInfo, MediumCategoryInfo, SubCategoryInfo, PurchaseDetails, ViewDetails
from .serializers import ProductSerializer, PurchaseDetailsSerializer, ViewDetailsSerializer

from datetime import date


# Create your views here.

# The actions provided by the ModelViewSet class are 
# .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductInfo.objects.order_by("-pk")
    serializer_class = ProductSerializer

    #create category json
    category_group = dict()
    main_categories = MainCategoryInfo.objects.all()
    medium_categories = MediumCategoryInfo.objects.all()
    sub_categories = SubCategoryInfo.objects.all()

    for main_cat in main_categories:
        category_group[main_cat.main_category_name] = dict()
        for med_cat in medium_categories:
            if med_cat.main_category_no.main_category_name in category_group:
                category_group[med_cat.main_category_no.main_category_name][med_cat.medium_category_name] = []

                for sub_cat in sub_categories:
                    if sub_cat.medium_category_no.medium_category_name in category_group[med_cat.main_category_no.main_category_name]:
                        category_group[med_cat.main_category_no.main_category_name][sub_cat.medium_category_no.medium_category_name].append(sub_cat.sub_category_name)

    
    # general view override -----------------------------------------------------------


    # 전체 상품 목록 / 검색
    def list(self, request, *args, **kwargs):
        main_category = request.GET.get('mainCategory',None)
        medium_category = request.GET.get('mediumCategory', None)
        search_word = request.GET.get('content', None)
        
        products = self.queryset

        if main_category:
            products = products.filter(main_category_no=main_category)
            if medium_category:
                products = products.filter(medium_category_no=medium_category)
        if search_word:

            products = products.filter(title__icontains=search_word)

        serializer = self.serializer_class(products, many=True)

        return Response(serializer.data)


    #상품 등록
    def create(self, request, *args, **kwargs):
        #로그인된 사용자일 경우에만
        username = request.META["HTTP_X_USERNAME"]
        if username != 'anonymousUser':
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid(raise_exception=True):
                
                serializer.save()
                return Response(status=200)
        else:
            return Response("NO USER")

    #상품 수정
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

    #상품 삭제
    def destroy(self, request, pk):
        username = request.META["HTTP_X_USERNAME"]
        instance = get_object_or_404(ProductInfo, no=pk)
        writer = instance.writer.username
        pk = pk
        if username == writer:
            instance.delete()
            return Response(status=204)
        else:
            return Response("NO AUTHORIZATION")
    

    
    # custom functions -----------------------------------------------------------------
    @action(detail=False)
    def get_latest_products(self, reqeust):
        latest_queryset = self.queryset[:3]
        serialzier = self.serializer_class(latest_queryset, many=True)
        return Response(serialzier.data)

    
    @action(detail=True, methods=["POST"] )
    def viewed(self, request, pk=None):
        username = request.META["HTTP_X_USERNAME"]
        # product_no = request.data["product_no"]
        product_no = pk
        sub_category_no = request.data["sub_category_no"]
        # print(product_no, sub_category_no)
        today = date.today()
        serializer = ViewDetailsSerializer(data={"user":username, "product_no":product_no, "sub_category_no":sub_category_no, "reg_time":today})
        if serializer.is_valid(raise_exception=True):
            today_viewed_products = ViewDetails.objects.filter(reg_time__date=today)

            if not today_viewed_products.filter(user=username, product_no=product_no, sub_category_no=sub_category_no).exists():
                serializer.save()
                return Response(status=200)
            return Response("already viewed")
    
    @action(detail=False)
    def top_three_viewed_today(self, reqeust):
        today = date.today()
        today_viewed_products = ViewDetails.objects.filter(reg_time__date=today) # 오늘 조회
        queryset = today_viewed_products.values('product_no_id').annotate(count=Count('product_no_id')).values('product_no_id')
        queryset = queryset.order_by("-count")
        queryset = queryset[:3]
        top_product_ids = []
        
        for q in queryset:
            top_product_ids.append(q["product_no_id"])
        
        top_products = ProductInfo.objects.filter(no__in=top_product_ids)
        serializer = self.serializer_class(top_products, many=True)
        return Response(serializer.data, status=200)



        



    @action(detail=False)
    def recommendation(self, request):
        # 상품 추천 로직
        # 추천 상품 목록 리턴
        pass
    
    @action(methods=["POST"], detail=True)
    def sold(self, request):
        # 요청 보내는 사람과 판매글 작성자가 같은지 확인
        
        username = request.META["HTTP_X_USERNAME"]
        product_no = request.GET.get("product_no")

        buyer = request.data["buyer"]
        product = self.queryset.get(pk=product_no)
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
        
        return Response(self.category_group)
        
        



    

    

