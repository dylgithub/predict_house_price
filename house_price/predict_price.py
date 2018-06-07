##-*- coding=utf-8 -*-
import pandas as pd
import xgboost as gbt
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score
import pickle
from sklearn.model_selection import GridSearchCV
from xgboost import plot_importance
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from house_price import get_feature
def index_demo():
    test_df = pd.read_csv('result.csv',index_col='id')
    print(test_df.head(2))
def get_year(datas):
    datas=dt.datetime.strptime(datas,'%Y.%m.%d')
    return datas.year
def get_month(datas):
    datas=dt.datetime.strptime(datas,'%Y.%m.%d')
    return datas.month
def get_subway_length(length):
    if length>0 and length<=1000:
        return 0
    elif length>1000 and length<=2000:
        return 1
    elif length>2000 and length<3000:
        return 2
    else:
        return 3
'''
数据处理
'''
def data_process():
    df = pd.read_csv('result.csv',index_col='id')
    house_price = df['totalPrice']
    df = df.drop(['totalPrice','unitPrice'], axis=1)
    df2 = pd.read_csv('beijingsale.csv', encoding='gb2312',index_col='id')
    df['sale_time'] = df2['dealDate']
    df['sale_year'] = df['sale_time'].apply(get_year)
    df['sale_month'] = df['sale_time'].apply(get_month)
    df.drop(['sale_time'], axis=1, inplace=True)
    df['dealHouseTxt']=df['dealHouseTxt'].apply(get_subway_length)
    print(df.head(1))
    #这里注意要只获得values值
    return df.values,house_price.values
model_file_name='house_model.pkl'
#训练模型并保持
def train_model():
    data, label = data_process()
    model = gbt.XGBRegressor(n_estimators=1000, subsample=0.8, learning_rate=0.25, objective='reg:tweedie')
    model.fit(data,label)
    with open(model_file_name,'wb') as fr:
        pickle.dump(model,fr)
#房价的预测函数
def price_predict(data_list):
    data_list=list(data_list)
    predict_data=[]
    jingdu=116
    weidu=39
    area=1
    house_area=get_feature.get_house_area(data_list[1])
    zhuangxiu=get_feature.get_decorate(data_list[2])
    si,ting=get_feature.get_siting_data(data_list[3])
    house_heigh=get_feature.get_house_high(data_list[4])
    predict_data.append(house_area)
    predict_data.append(1)
    predict_data.append(zhuangxiu)
    predict_data.append(1)
    predict_data.append(2)
    predict_data.append(house_heigh)
    predict_data.append(jingdu)
    predict_data.append(weidu)
    predict_data.append(si)
    predict_data.append(area)
    predict_data.append(ting)
    predict_data.append(2018)
    predict_data.append(5)
    predict_data=list(map(float,predict_data))
    predict_data=np.array([predict_data])
    with open(model_file_name,'rb') as fr:
        model=pickle.load(fr)
    yHat=model.predict(predict_data)
    # print(yHat[0])
    return yHat[0]
def model_run():
    data,label=data_process()
    X_train,X_val,y_train,y_val=train_test_split(data,label,test_size=0.2)
    model=gbt.XGBRegressor(n_estimators=1000,subsample=0.8,learning_rate=0.25,objective='reg:tweedie')
    # params=dict(learning_rate=[0.2,0.25,0.3,0.35],min_child_weight=[1,2,3])
    # grid_search=GridSearchCV(model,param_grid=params)
    # grid_search.fit(X_train,y_train)
    # print(grid_search.best_params_)
    # plot_importance(model)
    # plt.show()
    model.fit(X_train, y_train)
    with open(model_file_name,'wb') as fr:
        pickle.dump(model,fr)
    with open(model_file_name,'rb') as fr2:
        load_model=pickle.load(fr2)
    yHat = load_model.predict(X_val)
    print(explained_variance_score(y_val, yHat))
if __name__ == '__main__':
    # data_process()
    data_list=['朝阳区','一百二十一平','需要','想要三居室一厅的','想要中层的']
    print(price_predict(data_list))