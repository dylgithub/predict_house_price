#encoding=utf-8
import jieba
from house_price import data_helper
strs='地下室,底层，中层，高层'
strs2='不用'
strs3='我需要'
strs4='不需要'
#获取是否精装修数据
def get_decorate(strs):
    jieba.suggest_freq("不需要", True)
    cut_list = list(jieba.cut(strs))
    if '是' in cut_list:
        return 1
    elif '需要' in cut_list:
        return 1
    elif '用' in cut_list:
        return 1
    elif '不是' in cut_list:
        return 0
    elif '不需要' in cut_list:
        return 0
    elif '不用' in cut_list:
        return 0
    else:
        return 0
common_used_numerals_tmp = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
                                '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
delete_list = []
for key in common_used_numerals_tmp.keys():
    delete_list.append(key)
for i in range(10):
    delete_list.append(str(i))
#获取房屋面积
def get_house_area(strs):
    start=end=10000
    for i,data in enumerate(strs):
        if data in delete_list:
            if start==10000:
                start=i
        if data not in delete_list:
            if end==10000:
                end=i
    strs=strs[start:end]
    print(type(data_helper.get_chinese2num(strs)))
    return data_helper.get_chinese2num(strs)
#获取房屋楼层高度数据
def get_house_high(strs):
    cut_list=list(jieba.cut(strs))
    if '地下室' in cut_list:
        return 1
    elif '低层' in cut_list:
        return 2
    elif '中层' in cut_list:
        return 3
    elif '高层' in cut_list:
        return 4
    else:
        return 3
#获取几居室几厅的数据
def get_siting_data(strs):
    flag1 = flag2 = False
    jusi=ting=2
    for i, data in enumerate(strs):
        if data in delete_list:
            if flag1 == False:
                flag1 = True
                jusi=data_helper.get_chinese2num(data)
            else:
                if flag2 == False:
                    flag2 = True
                    ting = data_helper.get_chinese2num(data)
    return jusi,ting
# strs5='两室三厅'
# jusi,ting=get_siting_data(strs5)
# print(jusi,ting)
# print(get_house_area('九十六平'))
