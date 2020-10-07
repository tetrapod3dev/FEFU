from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse

from .models import ViewDetails, User, SubCategoryInfo, MediumCategoryInfo, ProductInfo, MainCategoryInfo
from .serializers import ViewDetailsSerializer, UserSerializer, MediumCategoryInfoSerializer, SubCategoryInfoSerializer, MainCategoryInfoSerializer
from .recommend.recommendations import recom_simple, recom_ibcf

import pandas as pd
import numpy as np
import pickle
import os

# dummy data를 불러옵니다. (유저-카테고리-조회수)
dataframes = pd.read_pickle(os.path.dirname(os.path.realpath(__file__)) + '/recommend/recommend_data/user_category_dummy.pkl')

df_counts = dataframes['view_counts']
df_users = dataframes['users']

# # key: 카테고리 no / values: 카테고리명으로 구성된 dictionary입니다.
with open(os.path.dirname(os.path.realpath(__file__)) + '/recommend/recommend_data/category_dict.pkl', 'rb') as handle:
    category_dict = pickle.load(handle)

item_similarity = pd.read_pickle(os.path.dirname(os.path.realpath(__file__)) + '/recommend/recommend_data/item_similarity.pkl')

sub_to_med = {1: 1, 2: 1, 3: 1, 4: 1, 11: 2, 12: 2, 13: 2, 14: 2, 21: 3, 31: 21, 32: 21, 33: 21, 34: 21, 35: 21, 41: 22, 42: 22, 43: 22, 44: 22, 45: 22, 51: 23, 52: 23, 61: 24, 62: 24, 63: 24, 71: 25, 72: 25, 73: 25, 81: 26, 82: 26, 83: 26, 91: 27, 92: 27, 93: 27, 101: 28, 102: 28, 103: 28, 104: 28, 105: 28, 111: 29, 112: 29, 113: 29, 114: 29, 115: 29, 116: 29, 121: 30, 122: 30, 123: 30, 131: 31, 132: 31, 133: 31, 141: 32, 142: 32, 151: 33, 152: 33, 153: 33, 161: 34, 162: 34, 163: 34, 164: 34, 165: 34, 171: 35, 181: 41, 182: 41, 183: 41, 191: 42, 192: 42, 193: 42, 194: 42, 201: 43, 202: 43, 203: 43, 204: 43, 205: 43, 211: 44, 212: 44, 213: 44, 214: 44, 215: 44, 221: 45, 222: 45, 223: 45, 224: 45, 231: 46, 232: 46, 233: 46, 234: 46, 235: 46, 236: 46, 241: 47, 242: 47, 243: 47, 244: 47, 251: 48, 252: 48, 253: 48, 254: 48, 255: 48, 261: 49, 262: 49, 263: 49, 264: 49, 271: 50, 272: 50, 273: 50, 274: 50, 281: 51, 282: 51, 283: 51, 291: 52, 292: 52, 293: 52, 301: 53, 311: 61, 312: 61, 313: 61, 314: 61, 315: 61, 316: 61, 321: 62, 322: 62, 323: 62, 331: 63, 332: 63, 333: 63, 334: 63, 335: 63, 336: 63, 341: 64, 342: 64, 351: 65, 352: 65, 361: 66, 362: 66, 363: 66, 364: 66, 365: 66, 366: 66, 367: 66, 368: 66, 371: 67, 372: 67, 373: 67, 374: 67, 381: 68, 382: 68, 383: 68, 384: 68, 385: 68, 386: 68, 387: 68, 388: 68, 391: 69, 392: 69, 393: 69, 394: 69, 401: 70, 402: 70, 403: 70, 411: 71, 412: 71, 413: 71, 421: 72, 422: 72, 423: 72, 424: 72, 431: 81, 432: 81, 433: 81, 441: 82, 442: 82, 443: 82, 444: 82, 451: 83, 452: 83, 453: 83, 454: 83, 461: 84, 462: 84, 463: 84, 464: 84, 471: 85, 472: 85, 473: 85, 481: 86, 482: 86, 483: 86, 484: 86, 491: 101, 492: 101, 493: 101, 494: 101, 501: 102, 502: 102, 503: 102, 511: 103, 512: 103, 513: 103, 521: 104, 522: 104, 523: 104, 531: 105, 532: 105, 533: 105, 534: 105, 535: 105, 541: 106, 542: 106, 543: 106, 551: 107, 552: 107, 561: 108, 562: 108, 563: 108, 564: 108, 571: 109, 572: 109, 573: 109, 581: 110, 582: 110, 583: 110, 591: 111, 592: 111, 601: 112, 602: 112, 603: 112, 604: 112, 611: 113, 612: 113, 613: 113, 614: 113, 621: 121, 622: 121, 623: 121, 631: 122, 632: 122, 633: 122, 641: 123, 642: 123, 643: 123, 651: 124, 652: 124, 653: 124, 654: 124, 655: 124, 656: 124, 661: 125, 662: 125, 663: 125, 664: 125, 671: 126, 672: 126, 673: 126, 674: 126, 681: 127, 682: 127, 683: 127, 684: 127, 691: 128, 692: 128, 693: 128, 694: 128, 695: 128, 701: 129, 702: 129, 703: 129, 711: 130, 712: 130, 713: 130, 714: 130, 715: 130, 716: 130, 717: 130, 718: 130, 721: 131, 722: 131, 723: 131, 724: 131, 725: 131, 731: 132, 732: 132, 733: 132, 734: 132, 741: 133, 742: 133, 743: 133, 751: 134, 752: 134, 753: 134, 761: 135, 762: 135, 763: 135, 771: 136, 772: 136, 773: 136, 774: 136, 775: 136, 781: 141, 782: 141, 783: 141, 791: 142, 792: 142, 793: 142, 794: 142, 795: 142, 796: 142, 801: 143, 802: 143, 803: 143, 811: 144, 812: 144, 813: 144, 821: 145, 822: 145, 823: 145, 831: 146, 832: 146, 833: 146, 834: 146, 835: 146, 841: 147, 842: 147, 843: 147, 851: 148, 852: 148, 853: 148, 854: 148, 855: 148, 856: 148, 861: 161, 862: 161, 863: 161, 871: 162, 872: 162, 873: 162, 874: 162, 881: 163, 882: 163, 883: 163, 891: 164, 892: 164, 893: 164, 894: 164, 895: 164, 901: 165, 902: 165, 903: 165, 904: 165, 905: 165, 911: 166, 912: 166, 913: 166, 914: 166, 921: 167, 922: 167, 923: 167, 924: 167, 931: 168, 932: 168, 933: 168, 934: 168, 941: 169, 942: 169, 943: 169, 951: 170, 952: 170, 953: 170, 961: 171, 962: 171, 963: 171, 964: 171, 965: 171, 966: 171, 971: 181, 972: 181, 973: 181, 974: 181, 981: 182, 982: 182, 983: 182, 991: 183, 992: 183, 993: 183, 994: 183, 1001: 184, 1002: 184, 1003: 184, 1011: 185, 1012: 185, 1013: 185, 1021: 186, 1022: 186, 1023: 186, 1024: 186, 1031: 187, 1032: 187, 1033: 187, 1034: 187, 1041: 188, 1042: 188, 1043: 188, 1051: 189, 1052: 189, 1053: 189, 1061: 190, 1071: 201, 1072: 201, 1073: 201, 1074: 201, 1075: 201, 1076: 201, 1077: 201, 1078: 201, 1079: 201, 1081: 202, 1082: 202, 1083: 202, 1084: 202, 1091: 203, 1092: 203, 1093: 203, 1094: 203, 1101: 204, 1102: 204}


def transform_gender(gender):
    """
        gender를 M 또는 F로 변경합니다. (남자 / 여자 => M / F)
    """
    return 'M' if (gender == '남자') else 'F'

def transform_age(age):
    """
        유저의 실제 나이를 연령대로 변환합니다. (17 => 10 / 21 => 20)
    """
    return (age // 10) * 10

def recommend(request, user_pk):
    user = get_object_or_404(User, no=user_pk)

    # dummy data(views)와 DB의 유저-카테고리-조회수를 합치는 작업입니다.
    viewDetails = ViewDetails.objects.all()
    view_serializer = ViewDetailsSerializer(viewDetails, many=True)

    db_view_data = [[x['user'], x['sub_category_no'], 1] for x in view_serializer.data]
    df_db_view_data = pd.DataFrame(db_view_data, columns=['user', 'category', 'count'])
    
    # dummy data(users)와 DB의 유저 정보를 합치는 작업입니다.
    users = User.objects.all()
    users_serializer = UserSerializer(users, many=True)

    db_user_data = [[x['username'], x['gender'], x['age']] for x in users_serializer.data]
    df_db_user_data = pd.DataFrame(db_user_data, columns=['user', 'gender', 'age'])
    df_db_user_data['gender'] = df_db_user_data['gender'].apply(transform_gender)
    df_db_user_data['age'] = df_db_user_data['age'].apply(transform_age)

    new_df_counts = df_counts.append(df_db_view_data)
    new_df_users = df_users.append(df_db_user_data)
    new_df_counts = new_df_counts.groupby(['user', 'category'])['count'].agg(['sum']).reset_index()
    # new_df_users : 모든 유저 정보 (username, age, gender)
    # new_df_counts: 모든 유저의 카테고리별 조회수

    # 추천하고자하는 User의 중분류별 조회수를 계산합니다. (Simple or IBCF 분기용)
    user_view_data = df_db_view_data[df_db_view_data['user'] == user.username]
    user_view_data['med_category'] = user_view_data['category'].apply(lambda category: sub_to_med[category])
    user_view_data = user_view_data.groupby(['med_category'])['count'].sum().sort_values(ascending=False)
    size_med = user_view_data.size
    mean_med = user_view_data.mean()

    # 현재는 중분류 2개 이상, 모든 중분류 조회수의 평균값이 2이상으로 설정해두었습니다.
    # 추후 수정해야됩니다 (MF를 도입하여 Hybrid도입 시)
    if size_med >= 2 and mean_med >= 2:
        method = 'IBCF'
        user_info = {
            'username': user.username,
            'gender': transform_gender(user.gender),
            'age': transform_age(user.age)
        }
        results = recom_ibcf(user_info, new_df_counts, n_items=10)

    else:
        method = 'Simple'
        merged_df = pd.merge(new_df_users, new_df_counts, on='user')

        user_view_boolean = ViewDetails.objects.filter(user=user).exists()

        user_info = {
            'username': user.username,
            'gender': transform_gender(user.gender),
            'age': transform_age(user.age)
        }
        
        results = recom_simple(user_info, merged_df, user_view_boolean, n_items=10)
        results['category'] = results['category'].apply(lambda x: category_dict[x])

    print(results)

    return JsonResponse({'method': method, 'result': list(results['category'].values)})


def similar(request, product_pk):
    product = get_object_or_404(ProductInfo, no=product_pk)

    test = item_similarity.loc[product.sub_category_no.no].sort_values(ascending=False).reset_index()
    test['category'] = test['category'].apply(lambda x: category_dict[x])
    print(test)

    return JsonResponse({'result': 'result'})


# Create your views here.
def index(request):
    mains = MainCategoryInfoSerializer(MainCategoryInfo.objects.all(), many=True)
    meds = MediumCategoryInfoSerializer(MediumCategoryInfo.objects.all(), many=True)
    subs = SubCategoryInfoSerializer(SubCategoryInfo.objects.all(), many=True)

    categories = dict()
    categories['category'] = []
    for main in mains.data:
        categories['category'].append({'id': main['no'], 'name': main['main_category_name'], 'medium_categories': []})
    for med in meds.data:
        categories['category'][med['main_category_no']-1]['medium_categories'].append({'med_id': med['no'], 'med_name': med['medium_category_name'], 'sub_categoreis': []})

    for sub in subs.data:
        for main in categories['category']:
            for med in main['medium_categories']:
                if sub['medium_category_no'] == med['med_id']:
                    med['sub_categoreis'].append({'sub_id': sub['no'], 'sub_name': sub['sub_category_name']})
    
    return JsonResponse({'category': categories})



def ibcf_rec(request, user_pk):
    user = get_object_or_404(User, no=user_pk)

    viewDetails = ViewDetails.objects.all()
    view_serializer = ViewDetailsSerializer(viewDetails, many=True)
    db_view_data = [[x['user'], x['sub_category_no'], 1] for x in view_serializer.data]
    df_db_view_data = pd.DataFrame(db_view_data, columns=['user', 'category', 'count'])
    
    users = User.objects.all()
    users_serializer = UserSerializer(users, many=True)
    db_user_data = [[x['no'], x['gender'], x['age']] for x in users_serializer.data]
    df_db_user_data = pd.DataFrame(db_user_data, columns=['user', 'gender', 'age'])
    df_db_user_data['gender'] = df_db_user_data['gender'].apply(transform_gender)
    df_db_user_data['age'] = df_db_user_data['age'].apply(transform_age)

    new_df_counts = df_counts.append(df_db_view_data)
    new_df_users = df_users.append(df_db_user_data)

    user_view_data = df_db_view_data[df_db_view_data['user'] == user.username]
    user_view_data['med_category'] = user_view_data['category'].apply(lambda category: sub_to_med[category])
    user_view_data = user_view_data.groupby(['med_category'])['count'].sum().sort_values(ascending=False)
    print(user_view_data)

    new_df_counts = new_df_counts.groupby(['user', 'category'])['count'].agg(['sum']).reset_index()

    results = recom_ibcf({'username': user.username, 'gender': transform_gender(user.gender), 'age': transform_age(user.age)}, new_df_counts, n_items=10)
    
    return JsonResponse({'result': list(results['category'].values)})

