import random

# 남성 화장품
cosmetic_1 = [181, 182, 183, 191, 192, 193, 194, 201, 202, 203, 204, 205, 241, 242, 243, 244, 261, 262, 263, 264, 271, 272, 273, 274, 281, 282, 283, 292]
# 디지털 일부 항목 제외하고 전부
digital_1 = [311, 312, 313, 314, 315, 316, 321, 322, 323, 331, 332, 333, 334, 335, 336, 341, 342, 351, 352, 361, 362, 368, 371, 372, 373, 374, 381, 382, 383, 384, 385, 386, 387, 388]
# 디지털1에서 게임 제외
digital_2 = [311, 312, 313, 314, 315, 316, 321, 322, 323, 331, 332, 333, 334, 335, 336, 341, 342, 351, 352, 361, 362, 368, 371, 372, 373, 374]
# 레저 대부분
leisure_1 = [971, 972, 973, 974, 981, 982, 983, 991, 992, 993, 994, 1021, 1022, 1023, 1024, 1031, 1032, 1033, 1034, 1041, 1042, 1043]
# 남성 20대 스포츠
sports_20 = [861, 862, 863, 881, 882, 883, 891, 892, 893, 894, 911, 912, 913, 914, 901, 902, 903, 904, 931, 932, 933, 934, 941, 942, 943, 964]
# 남성 20대 레저
leisure_20 = [981, 982, 983, 991, 992, 993, 994, 1021, 1022, 1023, 1024, 871, 872, 873, 874]
# 가전제품 전부
home_appliance_all = [431, 432, 433, 441, 442, 443, 444, 451, 452, 453, 454, 461, 462, 463, 464, 471, 472, 473]
# 가구 전부
furniture_all = [491, 492, 493, 494, 501, 502, 503, 511, 512, 513, 521, 522, 523, 531, 532, 533, 534, 535, 541, 542, 543, 561, 562, 563, 564, 571, 572, 573, 581, 582, 583, 591, 592, 601, 602, 603, 604, 611, 612, 613, 614]
# 유아 전부
kid_all = [781, 782, 783, 791, 792, 793, 794, 795, 796, 801, 802, 803, 811, 812, 813, 821, 822, 823, 831, 832, 833, 834, 835, 851, 852, 853, 854, 855, 856]
# 남성 40대 레저
leisure_40 = [971, 972, 973, 974, 981, 982, 983, 991, 992, 993, 994, 1001, 1003, 1011, 1012, 1013, 871, 872, 873, 874]
sports_50 = [861, 862, 863, 881, 882, 883, 891, 892, 893, 894, 895, 901, 902, 903, 904, 905, 931, 932, 933, 934, 941, 942, 943, 951, 952, 953, 961, 962, 963, 964, 965, 966]

# 10대 화장품(전부)
cosmetic_all = [181, 182, 183, 191, 192, 193, 194, 201, 202, 203, 204, 205, 211, 212, 213, 214, 215, 221, 222, 223, 224, 231, 232, 233, 234, 235, 236, 241, 242, 243, 244, 251, 252, 253, 254, 255, 261, 262, 263, 264, 271, 272, 273, 274, 291, 293]
fashion_f_default = [1, 2, 31, 32, 33, 34, 71, 82, 83, 91, 93, 111, 112, 113, 114, 115, 116, 121, 131, 141, 161, 163]
leisure_f_default = [971, 972, 973, 974, 981, 982, 983, 991, 992, 993, 994, 1011, 1012, 1013, 1021, 1022, 1023, 1024, 1041, 1042, 1043, 1051, 1052, 1053]
home_appliance_all_2 = home_appliance_all + [481, 482, 483, 484]
fashion_all = [1, 2, 3, 4, 11, 12, 13, 14, 21, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 61, 62, 63, 71, 72, 73, 82, 83, 91, 92, 93, 101, 102, 103, 104, 105, 111, 112, 113, 114, 115, 116, 121, 122, 123, 131, 132, 133, 141, 142]
living_all = [641, 642, 643, 651, 652, 653, 654, 655, 656, 661, 662, 663, 664, 691, 692, 693, 694, 695, 701, 702, 703, 721, 722, 723, 724, 725, 731, 732, 733, 734, 741, 742, 743, 751, 752, 753, 761, 762, 763]

only_fashion = [1, 2, 3, 4, 11, 12, 13, 14, 21]
only_fancy = [31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 61, 62, 63, 71, 72, 73, 82, 83, 91, 92, 93, 101, 102, 103, 104, 105, 111, 112, 113, 114, 115, 116, 121, 122, 123, 131, 132, 133, 141, 142]

dummy_data = {
    'male_10_1' : {
        'user_id': list(range(90001, 90021)),
        'gender': 'M',
        'age': 10,
        'main_category': [1072, 1073, 1075, 1091, 1092, 1094],
        'sub1_category': list(range(311, 317)) + list(range(331, 337)),
        'sub2_category': [891, 892, 901, 902, 911, 912, 941],
        'etc_category': [11, 12, 42, 43, 72, 152, 313, 652, 654, 655]
    },

    'male_10_2' : {
        'user_id': list(range(90021, 90041)),
        'gender': 'M',
        'age': 10,
        'main_category': [861, 862, 882, 891, 892, 901, 902, 911, 912],
        'sub1_category': [11, 12, 42, 43, 52, 92, 132, 72],
        'sub2_category': [1072, 1073, 1074],
        'etc_category': [111, 122, 162, 191, 313, 314, 893, 894, 895, 904, 905, 931, 932, 933, 934, 941, 942, 943, 913 ,914, 921, 922, 923, 924, 991, 993, 994]
    },

    'male_10_3' : {
        'user_id': list(range(90041, 90061)),
        'gender': 'M',
        'age': 10,
        'main_category': [11, 12, 42, 43, 52, 92, 72, 122, 132, 162, 321, 322],
        'sub1_category': [671, 672, 673, 674],
        'sub2_category': [891, 892, 901, 902, 911, 912],
        'etc_category': [1076, 1077, 1079]
    },

    'male_10_4' : {
        'user_id': list(range(90061, 90081)),
        'gender': 'M',
        'age': 10,
        'main_category': digital_1,
        'sub1_category': [1072, 1073, 1079, 1091, 1092],
        'sub2_category': [11, 12, 42, 43, 92, 72],
        'etc_category': []
    },

    'male_20_1' : {
        'user_id': list(range(90081, 90101)),
        'gender': 'M',
        'age': 20,
        'main_category': [11, 12, 41, 42, 43, 52, 63, 72, 92, 122, 132, 162, 321, 322],
        'sub1_category': [102, 103, 111, 113] + cosmetic_1,
        'sub2_category': leisure_1,
        'etc_category': []
    },

    'male_20_2' : {
        'user_id': list(range(90101, 90121)),
        'gender': 'M',
        'age': 20,
        'main_category': digital_1,
        'sub1_category': [1072, 1073, 1078, 1079, 1091, 1092, 1081, 1082, 1083, 1084],
        'sub2_category': [621, 622, 623, 631, 632, 633],
        'etc_category': []
    },

    'male_20_3' : {
        'user_id': list(range(90121, 90141)),
        'gender': 'M',
        'age': 20,
        'main_category': [1072, 1075, 1076, 1078, 1079, 1091, 1092, 1094],
        'sub1_category': [11, 12, 41, 42, 43, 72, 92],
        'sub2_category': digital_2,
        'etc_category': []
    },

    'male_20_4' : {
        'user_id': list(range(90141, 90161)),
        'gender': 'M',
        'age': 20,
        'main_category': sports_20,
        'sub1_category': leisure_20,
        'sub2_category': [11, 12, 41, 42, 43, 52, 63, 72, 92, 122, 132, 162, 321, 322],
        'etc_category': []
    },

    'male_30_1' : {
        'user_id': list(range(90161, 90181)),
        'gender': 'M',
        'age': 30,
        'main_category': digital_1,
        'sub1_category': home_appliance_all,
        'sub2_category': [1072, 1073, 1079, 631, 632, 633],
        'etc_category': []
    },

    'male_30_2' : {
        'user_id': list(range(90181, 90201)),
        'gender': 'M',
        'age': 30,
        'main_category': [1072, 1073, 1074, 1075, 1076, 1078, 1079, 1091, 1092, 1093, 1094],
        'sub1_category': [11, 12, 41, 42, 43, 44, 63, 72, 92, 122, 132, 162, 321, 322],
        'sub2_category': digital_2,
        'etc_category': []
    },

    'male_30_3' : {
        'user_id': list(range(90201, 90221)),
        'gender': 'M',
        'age': 30,
        'main_category': kid_all,
        'sub1_category': home_appliance_all,
        'sub2_category': furniture_all,
        'etc_category': []
    },

    'male_40_1' : {
        'user_id': list(range(90221, 90241)),
        'gender': 'M',
        'age': 40,
        'main_category': [1072, 1073, 1074, 1075, 1076, 1078, 1079, 1091, 1092, 1093, 1094],
        'sub1_category': [11, 12, 41, 42, 43, 44, 45, 63, 72, 92, 122, 132, 162, 321, 322],
        'sub2_category': leisure_40,
        'etc_category': []
    },

    'male_40_2' : {
        'user_id': list(range(90241, 90261)),
        'gender': 'M',
        'age': 40,
        'main_category': furniture_all,
        'sub1_category': home_appliance_all,
        'sub2_category': [331, 332, 333, 334, 335, 336, 361, 362, 363, 364, 365, 366, 367, 368],
        'etc_category': []
    },

    'male_40_3' : {
        'user_id': list(range(90261, 90281)),
        'gender': 'M',
        'age': 40,
        'main_category': [1071, 1072, 1073, 1074, 1075, 1076, 1077, 1079, 1091, 1092, 1093],
        'sub1_category': [311, 312, 313, 314, 315, 316, 321, 322, 323, 331, 332, 333, 334, 335, 336, 341, 342, 351, 352, 361, 362, 363, 364, 365, 366, 367, 368, 371, 372, 373, 374, 381, 382, 383, 384, 385, 386, 387, 388],
        'sub2_category': [621, 622, 623, 631, 632, 633, 641, 642, 643, 651, 652, 653, 654, 655, 656, 661, 662, 663, 664, 691, 692, 693, 694, 695, 701, 702, 703, 721, 722, 723, 724, 725, 731, 732, 733, 734, 741, 742, 743, 751, 752, 753, 761, 762, 763, 771, 772, 773, 774, 775],
        'etc_category': []
    },

    'male_50_1' : {
        'user_id': list(range(90281, 90301)),
        'gender': 'M',
        'age': 50,
        'main_category': list(range(1072, 1080)) + list(range(1091, 1095)),
        'sub1_category': [11, 12, 41, 42, 43, 44, 45, 51, 52, 63, 122, 132, 162, 103, 142],
        'sub2_category': [],
        'etc_category': []
    },

    'male_50_2' : {
        'user_id': list(range(90301, 90321)),
        'gender': 'M',
        'age': 50,
        'main_category': furniture_all,
        'sub1_category': home_appliance_all,
        'sub2_category': list(range(1072, 1080)) + list(range(1091, 1095)),
        'etc_category': []
    },

    'male_50_3' : {
        'user_id': list(range(90321, 90341)),
        'gender': 'M',
        'age': 50,
        'main_category': leisure_40,
        'sub1_category': sports_50,
        'sub2_category': list(range(711, 719)),
        'etc_category': []
    },

    'male_60_1' : {
        'user_id': list(range(90341, 90361)),
        'gender': 'M',
        'age': 60,
        'main_category': furniture_all,
        'sub1_category': home_appliance_all,
        'sub2_category': list(range(711, 719)),
        'etc_category': []
    },

    'male_60_2' : {
        'user_id': list(range(90361, 90381)),
        'gender': 'M',
        'age': 60,
        'main_category': list(range(711, 719)),
        'sub1_category': [971, 972, 973, 974, 981, 982, 983, 991, 992, 993, 994, 1001, 1002, 1003, 1011, 1012, 1013],
        'sub2_category': list(range(1071, 1080)) + list(range(1091, 1095)),
        'etc_category': []
    },

    'male_60_3' : {
        'user_id': list(range(90381, 90401)),
        'gender': 'M',
        'age': 60,
        'main_category': [971, 972, 973, 974, 981, 982, 983, 991, 992, 993, 994, 1001, 1002, 1003, 1011, 1012, 1013],
        'sub1_category': sports_50,
        'sub2_category': list(range(711, 719)),
        'etc_category': []
    },

    'male_70_1' : {
        'user_id': list(range(90401, 90421)),
        'gender': 'M',
        'age': 70,
        'main_category': furniture_all,
        'sub1_category': home_appliance_all,
        'sub2_category': list(range(1071, 1078)),
        'etc_category': []
    },

    'male_70_2' : {
        'user_id': list(range(90421, 90441)),
        'gender': 'M',
        'age': 70,
        'main_category': list(range(1071, 1078)) + list(range(1091, 1095)),
        'sub1_category': kid_all,
        'sub2_category': [],
        'etc_category': []
    },

    'male_70_3' : {
        'user_id': list(range(90441, 90461)),
        'gender': 'M',
        'age': 70,
        'main_category': [971, 972, 973, 974, 981, 982, 983, 991, 992, 993, 994, 1001, 1002, 1003, 1011, 1012, 1013],
        'sub1_category': list(range(711, 719)),
        'sub2_category': [],
        'etc_category': []
    },

    'female_10_1' : {
        'user_id': list(range(90501, 90521)),
        'gender': 'F',
        'age': 10,
        'main_category': digital_1,
        'sub1_category': [1072, 1073, 1079, 1091, 1092],
        'sub2_category': [1, 2, 32, 33, 71, 91, 93],
        'etc_category': []
    },

    'female_10_2' : {
        'user_id': list(range(90521, 90541)),
        'gender': 'F',
        'age': 10,
        'main_category': [1, 2, 32, 33, 34, 71, 82, 83, 91, 93, 111, 112, 113, 114, 115, 116, 121, 131, 141, 161, 163],
        'sub1_category': cosmetic_all,
        'sub2_category': list(range(1072, 1078)) + [1091, 1092],
        'etc_category': []
    },

    'female_10_3' : {
        'user_id': list(range(90541, 90561)),
        'gender': 'F',
        'age': 10,
        'main_category': [861, 862, 863, 901, 902, 903, 904, 905, 931, 932, 933, 934, 941, 942, 943],
        'sub1_category': [1, 2, 32, 33, 34, 71, 82, 83, 91, 93, 111, 112, 113, 114, 115, 116, 121, 131, 141, 161, 163],
        'sub2_category': [1072, 1073, 1074],
        'etc_category': []
    },

    'female_10_4' : {
        'user_id': list(range(90561, 90581)),
        'gender': 'F',
        'age': 10,
        'main_category': [1072, 1073, 1075, 1091, 1092, 1094],
        'sub1_category': [861, 862, 863, 901, 902, 903, 904, 905, 931, 932, 933, 934, 941, 942, 943],
        'sub2_category': [311, 312, 313, 314, 315, 316, 321, 322, 323, 341, 342, 351, 352],
        'etc_category': []
    },

    'female_20_1' : {
        'user_id': list(range(90581, 90601)),
        'gender': 'F',
        'age': 20,
        'main_category': fashion_f_default,
        'sub1_category': cosmetic_all,
        'sub2_category': [1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1091, 1092],
        'etc_category': []
    },

    'female_20_2' : {
        'user_id': list(range(90601, 90621)),
        'gender': 'F',
        'age': 20,
        'main_category': [1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1091, 1092],
        'sub1_category': fashion_f_default,
        'sub2_category': [311, 312, 313, 314, 315, 316, 321, 322, 323, 341, 342, 351, 352],
        'etc_category': []
    },

    'female_20_3' : {
        'user_id': list(range(90621, 90641)),
        'gender': 'F',
        'age': 20,
        'main_category': digital_1,
        'sub1_category': fashion_f_default,
        'sub2_category': list(range(1072, 1080)) + [1081, 1082, 1083, 1084, 1091, 1092, 1101, 1102],
        'etc_category': []
    },

    'female_20_4' : {
        'user_id': list(range(90641, 90661)),
        'gender': 'F',
        'age': 20,
        'main_category': [861, 862, 863, 881, 882, 883, 901, 902, 903, 904, 905, 921, 922, 923, 924, 931, 932, 933, 934, 941, 942, 943],
        'sub1_category': [631, 632, 633, 641, 642, 643, 651, 652, 653, 654, 655, 656, 671, 672, 673, 674, 721, 722, 723, 724, 725],
        'sub2_category': leisure_f_default,
        'etc_category': []
    },

    'female_30_1' : {
        'user_id': list(range(90661, 90681)),
        'gender': 'F',
        'age': 30,
        'main_category': fashion_f_default,
        'sub1_category': cosmetic_all,
        'sub2_category': [1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1091, 1092],
        'etc_category': []
    },

    'female_30_2' : {
        'user_id': list(range(90681, 90701)),
        'gender': 'F',
        'age': 30,
        'main_category': [1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1091, 1092],
        'sub1_category': fashion_f_default,
        'sub2_category': leisure_f_default,
        'etc_category': []
    },

    'female_30_3' : {
        'user_id': list(range(90701, 90721)),
        'gender': 'F',
        'age': 30,
        'main_category': kid_all + [841, 842, 843],
        'sub1_category':  [1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1091, 1092],
        'sub2_category': fashion_f_default,
        'etc_category': []
    },

    'female_40_1' : {
        'user_id': list(range(90721, 90741)),
        'gender': 'F',
        'age': 40,
        'main_category': list(range(1071, 1080)) + list(range(1081, 1085)) + [1091, 1092, 1101],
        'sub1_category': fashion_f_default,
        'sub2_category': [971, 972, 973, 974, 991, 992, 993, 994, 1011, 1012, 1013, 1051, 1052, 1053],
        'etc_category': []
    },

    'female_40_2' : {
        'user_id': list(range(90741, 90761)),
        'gender': 'F',
        'age': 40,
        'main_category': fashion_f_default,
        'sub1_category': cosmetic_all,
        'sub2_category': list(range(1071, 1080)) + list(range(1081, 1085)) + [1091, 1092, 1101],
        'etc_category': []
    },

    'female_40_3' : {
        'user_id': list(range(90761, 90781)),
        'gender': 'F',
        'age': 40,
        'main_category': furniture_all,
        'sub1_category': home_appliance_all_2,
        'sub2_category': list(range(1071, 1080)) + list(range(1081, 1085)) + [1091, 1092, 1101, 1102],
        'etc_category': []
    },

    'female_50_1' : {
        'user_id': list(range(90781, 90801)),
        'gender': 'F',
        'age': 50,
        'main_category': fashion_all,
        'sub1_category': cosmetic_all,
        'sub2_category': furniture_all,
        'etc_category': []
    },

    'female_50_2' : {
        'user_id': list(range(90801, 90821)),
        'gender': 'F',
        'age': 50,
        'main_category': home_appliance_all_2,
        'sub1_category': furniture_all,
        'sub2_category': living_all,
        'etc_category': []
    },

    'female_50_3' : {
        'user_id': list(range(90821, 90841)),
        'gender': 'F',
        'age': 50,
        'main_category': [971, 972, 973, 974, 991, 992, 993, 994, 1011, 1012, 1013, 1051, 1052, 1053],
        'sub1_category': [861, 862, 863, 871, 872, 873, 874, 881, 882, 883, 941, 942, 943, 951, 952, 953],
        'sub2_category': [711, 712, 713, 714, 715, 716, 717, 718],
        'etc_category': []
    },

    'female_60_1' : {
        'user_id': list(range(90841, 90861)),
        'gender': 'F',
        'age': 60,
        'main_category': only_fashion,
        'sub1_category': only_fancy,
        'sub2_category': furniture_all,
        'etc_category': []
    },

    'female_60_2' : {
        'user_id': list(range(90861, 90881)),
        'gender': 'F',
        'age': 60,
        'main_category': list(range(1071, 1080)) + [1091, 1092, 1093, 1094],
        'sub1_category': only_fashion,
        'sub2_category': only_fancy,
        'etc_category': []
    },

    'female_60_3' : {
        'user_id': list(range(90881, 90901)),
        'gender': 'F',
        'age': 60,
        'main_category': [971, 972, 973, 974, 991, 992, 993, 994, 1011, 1012, 1013, 1051, 1052, 1053, 861, 862, 863, 871, 872, 873, 874],
        'sub1_category': list(range(711, 719)),
        'sub2_category': list(range(1071, 1080)) + [1091, 1092, 1093, 1094],
        'etc_category': []
    },

    'female_70_1' : {
        'user_id': list(range(90901, 90921)),
        'gender': 'F',
        'age': 70,
        'main_category': home_appliance_all_2,
        'sub1_category': furniture_all,
        'sub2_category': living_all,
        'etc_category': []
    },

    'female_70_2' : {
        'user_id': list(range(90921, 90941)),
        'gender': 'F',
        'age': 70,
        'main_category': list(range(1071, 1080)) + list(range(1081, 1085)) + [1091, 1092, 1101, 1102],
        'sub1_category': kid_all,
        'sub2_category': [],
        'etc_category': []
    },

    'female_70_3' : {
        'user_id': list(range(90941, 90961)),
        'gender': 'F',
        'age': 70,
        'main_category': [971, 972, 973, 974, 991, 992, 993, 994, 1011, 1012, 1013, 1051, 1052, 1053, 861, 862, 863, 871, 872, 873, 874],
        'sub1_category': list(range(711, 719)),
        'sub2_category': list(range(1071, 1080)) + [1091, 1092, 1093, 1094],
        'etc_category': []
    }
}


raw_dummy_data = []
raw_user_data = []
for group in dummy_data.keys():
    for user in dummy_data[group]['user_id']:
        for main_category in dummy_data[group]['main_category']:
            raw_dummy_data.append([user, main_category, random.randrange(5)])
        for sub1_category in dummy_data[group]['sub1_category']:
            raw_dummy_data.append([user, sub1_category, random.randrange(4)])
        for sub2_category in dummy_data[group]['sub2_category']:
            raw_dummy_data.append([user, sub2_category, random.randrange(3)])
        for etc_category in dummy_data[group]['etc_category']:
            raw_dummy_data.append([user, etc_category, random.randrange(2)])
        raw_user_data.append([user, dummy_data[group]['gender'], dummy_data[group]['age']])


category1_all = [1, 2, 3, 4, 11, 12, 13, 14, 21]
category2_all = [31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 61, 62, 63, 71, 72, 73, 81, 82, 83, 91, 92, 93, 101, 102, 103, 104, 105, 111, 112, 113, 114, 115, 116, 121, 122, 123, 131, 132, 133, 141, 142, 151, 152, 153, 161, 162, 163, 164, 165, 171]
category3_all = [181, 182, 183, 191, 192, 193, 194, 201, 202, 203, 204, 205, 211, 212, 213, 214, 215, 221, 222, 223, 224, 231, 232, 233, 234, 235, 236, 241, 242, 243, 244, 251, 252, 253, 254, 255, 261, 262, 263, 264, 271, 272, 273, 274, 281, 282, 283, 291, 292, 293, 301]
category4_all = [311, 312, 313, 314, 315, 316, 321, 322, 323, 331, 332, 333, 334, 335, 336, 341, 342, 351, 352, 361, 362, 363, 364, 365, 366, 367, 368, 371, 372, 373, 374, 381, 382, 383, 384, 385, 386, 387, 388, 391, 392, 393, 394, 401, 402, 403, 411, 412, 413, 421, 422, 423, 424]
category5_all = [431, 432, 433, 441, 442, 443, 444, 451, 452, 453, 454, 461, 462, 463, 464, 471, 472, 473, 481, 482, 483, 484]
category6_all = [491, 492, 493, 494, 501, 502, 503, 511, 512, 513, 521, 522, 523, 531, 532, 533, 534, 535, 541, 542, 543, 551, 552, 561, 562, 563, 564, 571, 572, 573, 581, 582, 583, 591, 592, 601, 602, 603, 604, 611, 612, 613, 614]
category7_all = [621, 622, 623, 631, 632, 633, 641, 642, 643, 651, 652, 653, 654, 655, 656, 661, 662, 663, 664, 671, 672, 673, 674, 681, 682, 683, 684, 691, 692, 693, 694, 695, 701, 702, 703, 711, 712, 713, 714, 715, 716, 717, 718, 721, 722, 723, 724, 725, 731, 732, 733, 734, 741, 742, 743, 751, 752, 753, 761, 762, 763, 771, 772, 773, 774, 775]
category8_all = [781, 782, 783, 791, 792, 793, 794, 795, 796, 801, 802, 803, 811, 812, 813, 821, 822, 823, 831, 832, 833, 834, 835, 841, 842, 843, 851, 852, 853, 854, 855, 856]
category9_all = [861, 862, 863, 871, 872, 873, 874, 881, 882, 883, 891, 892, 893, 894, 895, 901, 902, 903, 904, 905, 911, 912, 913, 914, 921, 922, 923, 924, 931, 932, 933, 934, 941, 942, 943, 951, 952, 953, 961, 962, 963, 964, 965, 966]
category10_all = [971, 972, 973, 974, 981, 982, 983, 991, 992, 993, 994, 1001, 1002, 1003, 1011, 1012, 1013, 1021, 1022, 1023, 1024, 1031, 1032, 1033, 1034, 1041, 1042, 1043, 1051, 1052, 1053, 1061]
category11_all = [1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1081, 1082, 1083, 1084, 1091, 1092, 1093, 1094, 1101, 1102]

category_users = {
    'category_1': {
        'user_id': list(range(91001,91021)),
        'gender': 'C',
        'age': 100,
        'category': category1_all
    },
    'category_2': {
        'user_id': list(range(91021,91041)),
        'gender': 'C',
        'age': 100,
        'category': category2_all
    },
    'category_3': {
        'user_id': list(range(91041,91061)),
        'gender': 'C',
        'age': 100,
        'category': category3_all
    },
    'category_4': {
        'user_id': list(range(91061,91081)),
        'gender': 'C',
        'age': 100,
        'category': category4_all
    },
    'category_5': {
        'user_id': list(range(91081,91101)),
        'gender': 'C',
        'age': 100,
        'category': category5_all
    },
    'category_6': {
        'user_id': list(range(91101,91121)),
        'gender': 'C',
        'age': 100,
        'category': category6_all
    },
    'category_7': {
        'user_id': list(range(91121,91141)),
        'gender': 'C',
        'age': 100,
        'category': category7_all
    },
    'category_8': {
        'user_id': list(range(91141,91161)),
        'gender': 'C',
        'age': 100,
        'category': category8_all
    },
    'category_9': {
        'user_id': list(range(91161,91181)),
        'gender': 'C',
        'age': 100,
        'category': category9_all
    },
    'category_10': {
        'user_id': list(range(91181,91201)),
        'gender': 'C',
        'age': 100,
        'category': category10_all
    },
    'category_11': {
        'user_id': list(range(91201,91221)),
        'gender': 'C',
        'age': 100,
        'category': category11_all
    },
}

for category_group in category_users.keys():
    for user in category_users[category_group]['user_id']:
        for category in category_users[category_group]['category']:
            raw_dummy_data.append([user, category, 2])
        raw_user_data.append([user, category_users[category_group]['gender'], category_users[category_group]['age']])

# print(raw_dummy_data)
# print(raw_user_data)

import pandas as pd
import os

df = pd.DataFrame(data=raw_dummy_data, columns=['user', 'category', 'count'])
user_df = pd.DataFrame(data=raw_user_data, columns=['user', 'gender', 'age'])
# print(df)
# print(user_df)

df_new = df.groupby(['user', 'category'])['count'].sum().reset_index()
# print(df_new)

dataframes = {'view_counts': df_new, 'users': user_df}

pd.to_pickle(dataframes, 'dummy_data2.pkl')