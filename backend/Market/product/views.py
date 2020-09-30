from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .models import User, ProductInfo, MainCategoryInfo, MediumCategoryInfo, SubCategoryInfo, PurchaseDetails, ViewDetails
from .serializers import ProductSerializer, PurchaseDetailsSerializer, ViewDetailsSerializer, ProductDetailSerializer, MainCategoryInfoSerializer, MediumCategoryInfoSerializer, SubCategoryInfoSerializer

from datetime import date

#------Recommendation

import pandas as pd
import numpy as np
import pickle
import os

# Create your views here.

# The actions provided by the ModelViewSet class are 
# .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductInfo.objects.order_by("-pk")
    serializer_class = ProductSerializer


# category ----------------------------------------------------------------------
    @action(detail=False)
    def get_main_category(self, request):
        main_serializer = MainCategoryInfoSerializer(MainCategoryInfo.objects.all(), many=True)
        # print(main_serializer, "========================")
        return Response(main_serializer.data, status=200)

    @action(detail=False)
    def get_medium_category(self, request):
        main_no = request.GET.get('mainCategoryNo')
        medium_categories = MediumCategoryInfo.objects.filter(main_category_no=main_no)
        medium_serializer = MediumCategoryInfoSerializer(medium_categories, many=True)
        return Response(medium_serializer.data, status=200)

    @action(detail=False)
    def get_sub_category(self, request):
        med_no = request.GET.get('mediumCategoryNo')
        sub_categories = SubCategoryInfo.objects.filter(medium_category_no=med_no)
        sub_serializer = SubCategoryInfoSerializer(sub_categories, many=True)
        return Response(sub_serializer.data, status=200)

    
    # general view override -----------------------------------------------------------


    # 전체 상품 목록 / 검색
    def list(self, request, *args, **kwargs):
        main_category = request.GET.get('mainCategory',None)
        medium_category = request.GET.get('mediumCategory', None)
        search_word = request.GET.get('content', None)
        curPage = int(request.GET.get('pageNum', 1))
        
        products = self.queryset

        if main_category:
            products = products.filter(main_category_no=main_category)
            if medium_category:
                products = products.filter(medium_category_no=medium_category)
        if search_word:

            products = products.filter(title__icontains=search_word)

        perPageNum = 12 #페이지 당 글 수
        paginator = Paginator(products, perPageNum)
        totalCount = paginator.count # 글 개수
        
        curPage_products = paginator.get_page(curPage) #curPage의 글 목록
        startPage = 1 #시작 페이지
        endPage = paginator.num_pages #총 페이지 수
        prev_bool = curPage_products.has_previous()
        next_bool = curPage_products.has_next()
        startIndex = curPage_products.start_index()
        serializer = self.serializer_class(curPage_products, many=True)
        page = {"curPage":curPage, "perPageNum":perPageNum, "totalCount":totalCount, "startPage":startPage, "endPage":endPage, "prev":prev_bool, "next":next_bool, "startIndex":startIndex}
        return Response({"page":page, "list": serializer.data}, status=200)
    
    #상품 상세 정보 가져오기
    def retrieve(self, request, pk):
        product = self.queryset.get(no=pk)
        product_detail = ProductDetailSerializer(product)
        return Response(product_detail.data, status=200)




    #상품 등록
    def create(self, request, *args, **kwargs):
        #로그인된 사용자일 경우에만
        username = request.META["HTTP_X_USERNAME"]
        if username != 'anonymousUser':
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid(raise_exception=True):
                
                serializer.save()
                return Response("resource created successfully", status=201)
        else:
            return Response("unauthorized user", status=401)

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
            return Response("resource updated successfully", status=200)
        else:
            return Response("forbidden user", status=403)

    #상품 삭제
    def destroy(self, request, pk):
        username = request.META["HTTP_X_USERNAME"]
        instance = get_object_or_404(ProductInfo, no=pk)
        writer = instance.writer.username
        pk = pk
        if username == writer:
            instance.delete()
            return Response("resource deleted successfully", status=204)
        else:
            return Response("forbidden user", status=403)
    

    
    # custom functions -----------------------------------------------------------------
    @action(detail=False)
    def get_latest_products(self, reqeust):
        latest_queryset = self.queryset[:3]
        serialzier = self.serializer_class(latest_queryset, many=True)
        return Response(serialzier.data, status=200)

    
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
                return Response("resource created successfully", status=201)
            return Response("resource already created", status=200)
    
    @action(detail=False)
    def top_three_viewed_today(self, request):
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



    
    @action(methods=["PATCH"], detail=True)
    def sold(self, request, pk):
        # 요청 보내는 사람과 판매글 작성자가 같은지 확인
        username = request.META["HTTP_X_USERNAME"]
        # username = request.data["username"]
        buyer = request.data["buyer"]
        product = self.queryset.get(pk=pk)
        seller = product.writer.username
        status = product.status


        if username == seller:
            if status == 1: #팔 -> 안팔
                product_serializer = ProductSerializer(product, data={"status": 0}, partial=True)
                self.destroy_purchase(product.no)

            else: # 안팔 -> 팔
                product_serializer = ProductSerializer(product, data={"status": 1}, partial=True)
                self.create_purchase(pk, buyer, seller)               

            if product_serializer.is_valid():
                product_serializer.save()
                return Response("resource updated successfully", status=200)
        
        return Response("forbidden user", status=403)



    @action(detail=False)
    def categories(self, request):
        cat_group = self.category_group
        print(cat_group[("패션의류", 1)])
        return Response({"mini": cat_group[("패션의류", 1)]})
        

    def create_purchase(self, pk, buyer, seller):
        serializer = PurchaseDetailsSerializer(data={"seller":seller, "buyer":buyer, "product_no":pk})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("resource created successfully", status=201)
        
    
    def destroy_purchase(self, product_no):
        purchase_instance = get_object_or_404(PurchaseDetails, product_no=product_no)
        purchase_instance.delete()
        return Response("resource deleted successfully", status=204)


        # dummy data를 불러옵니다. (유저-카테고리-조회수)
    dataframes = pd.read_pickle(os.path.dirname(os.path.realpath(__file__)) + '/recommend/recommend_data/user_category_dummy.pkl')

    df_counts = dataframes['view_counts']
    df_users = dataframes['users']

    # # key: 카테고리 no / values: 카테고리명으로 구성된 dictionary입니다.
    with open(os.path.dirname(os.path.realpath(__file__)) + '/recommend/recommend_data/category_dict.pkl', 'rb') as handle:
        category_dict = pickle.load(handle)

    item_similarity = pd.read_pickle(os.path.dirname(os.path.realpath(__file__)) + '/recommend/recommend_data/item_similarity.pkl')

    sub_to_med = {1: 1, 2: 1, 3: 1, 4: 1, 11: 2, 12: 2, 13: 2, 14: 2, 21: 3, 31: 21, 32: 21, 33: 21, 34: 21, 35: 21, 41: 22, 42: 22, 43: 22, 44: 22, 45: 22, 51: 23, 52: 23, 61: 24, 62: 24, 63: 24, 71: 25, 72: 25, 73: 25, 81: 26, 82: 26, 83: 26, 91: 27, 92: 27, 93: 27, 101: 28, 102: 28, 103: 28, 104: 28, 105: 28, 111: 29, 112: 29, 113: 29, 114: 29, 115: 29, 116: 29, 121: 30, 122: 30, 123: 30, 131: 31, 132: 31, 133: 31, 141: 32, 142: 32, 151: 33, 152: 33, 153: 33, 161: 34, 162: 34, 163: 34, 164: 34, 165: 34, 171: 35, 181: 41, 182: 41, 183: 41, 191: 42, 192: 42, 193: 42, 194: 42, 201: 43, 202: 43, 203: 43, 204: 43, 205: 43, 211: 44, 212: 44, 213: 44, 214: 44, 215: 44, 221: 45, 222: 45, 223: 45, 224: 45, 231: 46, 232: 46, 233: 46, 234: 46, 235: 46, 236: 46, 241: 47, 242: 47, 243: 47, 244: 47, 251: 48, 252: 48, 253: 48, 254: 48, 255: 48, 261: 49, 262: 49, 263: 49, 264: 49, 271: 50, 272: 50, 273: 50, 274: 50, 281: 51, 282: 51, 283: 51, 291: 52, 292: 52, 293: 52, 301: 53, 311: 61, 312: 61, 313: 61, 314: 61, 315: 61, 316: 61, 321: 62, 322: 62, 323: 62, 331: 63, 332: 63, 333: 63, 334: 63, 335: 63, 336: 63, 341: 64, 342: 64, 351: 65, 352: 65, 361: 66, 362: 66, 363: 66, 364: 66, 365: 66, 366: 66, 367: 66, 368: 66, 371: 67, 372: 67, 373: 67, 374: 67, 381: 68, 382: 68, 383: 68, 384: 68, 385: 68, 386: 68, 387: 68, 388: 68, 391: 69, 392: 69, 393: 69, 394: 69, 401: 70, 402: 70, 403: 70, 411: 71, 412: 71, 413: 71, 421: 72, 422: 72, 423: 72, 424: 72, 431: 81, 432: 81, 433: 81, 441: 82, 442: 82, 443: 82, 444: 82, 451: 83, 452: 83, 453: 83, 454: 83, 461: 84, 462: 84, 463: 84, 464: 84, 471: 85, 472: 85, 473: 85, 481: 86, 482: 86, 483: 86, 484: 86, 491: 101, 492: 101, 493: 101, 494: 101, 501: 102, 502: 102, 503: 102, 511: 103, 512: 103, 513: 103, 521: 104, 522: 104, 523: 104, 531: 105, 532: 105, 533: 105, 534: 105, 535: 105, 541: 106, 542: 106, 543: 106, 551: 107, 552: 107, 561: 108, 562: 108, 563: 108, 564: 108, 571: 109, 572: 109, 573: 109, 581: 110, 582: 110, 583: 110, 591: 111, 592: 111, 601: 112, 602: 112, 603: 112, 604: 112, 611: 113, 612: 113, 613: 113, 614: 113, 621: 121, 622: 121, 623: 121, 631: 122, 632: 122, 633: 122, 641: 123, 642: 123, 643: 123, 651: 124, 652: 124, 653: 124, 654: 124, 655: 124, 656: 124, 661: 125, 662: 125, 663: 125, 664: 125, 671: 126, 672: 126, 673: 126, 674: 126, 681: 127, 682: 127, 683: 127, 684: 127, 691: 128, 692: 128, 693: 128, 694: 128, 695: 128, 701: 129, 702: 129, 703: 129, 711: 130, 712: 130, 713: 130, 714: 130, 715: 130, 716: 130, 717: 130, 718: 130, 721: 131, 722: 131, 723: 131, 724: 131, 725: 131, 731: 132, 732: 132, 733: 132, 734: 132, 741: 133, 742: 133, 743: 133, 751: 134, 752: 134, 753: 134, 761: 135, 762: 135, 763: 135, 771: 136, 772: 136, 773: 136, 774: 136, 775: 136, 781: 141, 782: 141, 783: 141, 791: 142, 792: 142, 793: 142, 794: 142, 795: 142, 796: 142, 801: 143, 802: 143, 803: 143, 811: 144, 812: 144, 813: 144, 821: 145, 822: 145, 823: 145, 831: 146, 832: 146, 833: 146, 834: 146, 835: 146, 841: 147, 842: 147, 843: 147, 851: 148, 852: 148, 853: 148, 854: 148, 855: 148, 856: 148, 861: 161, 862: 161, 863: 161, 871: 162, 872: 162, 873: 162, 874: 162, 881: 163, 882: 163, 883: 163, 891: 164, 892: 164, 893: 164, 894: 164, 895: 164, 901: 165, 902: 165, 903: 165, 904: 165, 905: 165, 911: 166, 912: 166, 913: 166, 914: 166, 921: 167, 922: 167, 923: 167, 924: 167, 931: 168, 932: 168, 933: 168, 934: 168, 941: 169, 942: 169, 943: 169, 951: 170, 952: 170, 953: 170, 961: 171, 962: 171, 963: 171, 964: 171, 965: 171, 966: 171, 971: 181, 972: 181, 973: 181, 974: 181, 981: 182, 982: 182, 983: 182, 991: 183, 992: 183, 993: 183, 994: 183, 1001: 184, 1002: 184, 1003: 184, 1011: 185, 1012: 185, 1013: 185, 1021: 186, 1022: 186, 1023: 186, 1024: 186, 1031: 187, 1032: 187, 1033: 187, 1034: 187, 1041: 188, 1042: 188, 1043: 188, 1051: 189, 1052: 189, 1053: 189, 1061: 190, 1071: 201, 1072: 201, 1073: 201, 1074: 201, 1075: 201, 1076: 201, 1077: 201, 1078: 201, 1079: 201, 1081: 202, 1082: 202, 1083: 202, 1084: 202, 1091: 203, 1092: 203, 1093: 203, 1094: 203, 1101: 204, 1102: 204}

        



    @action(detail=False)
    def recommendation(self, request):
        # 상품 추천 로직
        # 추천 상품 목록 리턴
        print(self.df_counts)
        return Response({"result": list(self.df_counts["user"].values) })


    

    

