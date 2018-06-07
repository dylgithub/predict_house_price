#encoding=utf-8
import pandas as pd
df=pd.read_csv('beijingsale2.csv',encoding='gbk')
title_list=list(df['title'].values)
cut_list=[i.split(' ') for i in title_list]
area_list=[i[0] for i in cut_list]
df['area']=area_list
def time_process(times):
    print(times)
    if times == '近30天内成交':
        times='2018.05.28'
    return times
dealDate_list=list(df['dealDate'])
for i,date in enumerate(dealDate_list):
    if date=='近30天内成交':
        dealDate_list[i]='2018.05.28'
# df['dealDate']=dealDate_list
df['dealDate']=df['dealDate'].apply(time_process)
print(df['dealDate'])
# print(area_list)
# print(cut_list)