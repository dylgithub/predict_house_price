#encoding=utf-8
import jieba
import jieba.posseg as pseg
import re
from math import pow
strs='中层楼'
#判断房屋楼层输入的合法性
def discrimination_house_high(strs):
    cut_list = list(jieba.cut(strs))
    print(cut_list)
    if '地下室' in cut_list:
        return 1
    elif '底层' in cut_list:
        return 1
    elif '中层' in cut_list:
        return 1
    elif '高层' in cut_list:
        return 1
    else:
        return 0
#判断房屋是否需要精装的合法性
def discrimination_decorate(strs):
    jieba.suggest_freq("不需要", True)
    cut_list = list(jieba.cut(strs))
    if '是' in cut_list:
        return 1
    elif '需要' in cut_list:
        return 1
    elif '用' in cut_list:
        return 1
    elif '不是' in cut_list:
        return 1
    elif '不需要' in cut_list:
        return 1
    elif '不用' in cut_list:
        return 1
    else:
        return 0
strs2='三十六平'
common_used_numerals_tmp = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
                            '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
delete_list = []
for key in common_used_numerals_tmp.keys():
    delete_list.append(key)
for i in range(10):
    delete_list.append(str(i))
#判断房屋大小输入的合法性
def discrimination_house_size(strs):
    for i, data in enumerate(strs):
        if data in delete_list:
            return 1
    return 0
strs4="两平米"
#判断房屋几居室几厅输入的合法性
def discrimination_siting(strs):
    flag1=flag2=False
    for i,data in enumerate(strs):
        if data in delete_list:
            if flag1==False:
                flag1=True
            else:
                if flag2==False:
                    flag2=True
    if flag1 and flag2:
        return 1
    else:
        return 0
strs3='我需要三室两厅的'
# print(discrimination_siting(strs3))
print(discrimination_house_high(strs))