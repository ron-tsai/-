import numpy as np
import pandas as pd
import numpy as np
import os
from tensorflow import keras
from matplotlib import pyplot as plt
from tensorflow.keras.models import Model
from tensorflow.keras import layers
from tensorflow.keras import Input
from sklearn.metrics import confusion_matrix,roc_curve, auc,recall_score,precision_score,f1_score
from tensorflow.keras.utils import plot_model

from sklearn.model_selection import train_test_split
import numpy as np



plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False

seed = 2

begin_date='2016-01-01'
end_date='2021-09-01'

validation_split=0.2

wenben_back=20
total_day=1338
train_num=1070
long_term_back=10

short_term_back=10
drop_num=0.2
wenben_sort=2
batch_size=32

epochs=40

LSTM_num=100
dense_num=20


# mix_file='666777-2.xlsx'
mix_file='东方关注777888.xlsx'
first_columns='search_index'



test_num=total_day-train_num






new_dir='/Users/ccmac/Documents/毕业论文数据/数据二合为一'
dir='/Users/ccmac/Documents/毕业论文数据/数据区间试验'
wenben_dir='/Users/ccmac/Documents/毕业论文数据/每日均值'
daily_df=pd.read_excel(os.path.join(new_dir,mix_file))
fif_df=pd.read_excel(os.path.join(dir,'fif_data.xlsx'))
target_df=pd.read_excel(os.path.join(dir,'target.xlsx'))
wenben_df=pd.read_excel(os.path.join(new_dir,mix_file))

begin=pd.to_datetime(begin_date)
end=pd.to_datetime(end_date)

daily_df=daily_df.loc[(daily_df['trade_time']>=begin)&(daily_df['trade_time']<=end),:].reset_index()
fif_df=fif_df.loc[(fif_df['trade_time']>=begin)&(fif_df['trade_time']<=end),:].reset_index()
target_df=target_df.loc[(target_df['trade_time']>=begin)&(target_df['trade_time']<=end),:].reset_index()
wenben_df=wenben_df.loc[(wenben_df['trade_time']>=begin)&(wenben_df['trade_time']<=end),:].reset_index()

print('数据长度',daily_df.shape)
print('数据索引',daily_df.index)


print('前几行',daily_df.head())
print('后几行',daily_df.tail())
print('切分数据位置',daily_df.loc[daily_df.index>=train_num,:])

print('fif_df',fif_df.head())
print('fif_df_tail',fif_df.tail())


def split_data(train_num=train_num,wenben_back=wenben_back):
    # print(daily_df.loc[daily_df.index<train_num])
    daily_train_df=daily_df.loc[daily_df.index<train_num]
    daily_test_df=daily_df.loc[daily_df.index>=train_num]
    fif_train_df=fif_df.loc[fif_df.index<16*train_num]
    fif_test_df=fif_df.loc[fif_df.index>=16*train_num]
    wenben_train_df=wenben_df.loc[wenben_df.index<train_num]
    wenben_test_df=wenben_df.loc[wenben_df.index>=train_num]

    target_train_df=target_df.loc[target_df.index<train_num] ##错target_train_df=target_df.loc[target_df.index<train_num-wenben_back]不应该减wenben_back
    target_test_df=target_df.loc[target_df.index>=train_num]




    return {'daily_train_df':daily_train_df,
            'daily_test_df':daily_test_df,
            'fif_train_df':fif_train_df,
            'fif_test_df':fif_test_df,
            'target_train_df':target_train_df,
            'target_test_df':target_test_df,
            'wenben_train_df':wenben_train_df,
            'wenben_test_df': wenben_test_df
            }







target_test_df=split_data()['target_test_df']
print('target_test_df',target_test_df)

husen300=target_test_df['close'][20:]
trade_time=target_test_df['trade_time'][20:]
print('沪深300指数测试区间',husen300)












# plot_model(model, show_shapes=True, show_layer_names=True)

# callback = keras.callbacks.EarlyStopping(monitor='loss', patience=2)#使用loss作为监测数据，轮数设置为1




























y_pred=[0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
y_pred2=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
y_pred1= [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]
class Back_tes_trader:
    def __init__(self,train_num,daily_back,wenben_back):
        self.train_num=train_num
        self.daily_back=daily_back
        self.wenben_back = wenben_back
    def daily_test_data(self,data):
        while True:
            samples = data.loc[
                data.index >=self.train_num+self.wenben_back ,
                ['open','close']]
            print(data.index)
            return samples

back_tes_trader=Back_tes_trader(train_num=train_num,daily_back=20,wenben_back=wenben_back)



def split_back_trader(train_num=train_num):

    daily_test_df=daily_df.loc[daily_df.index>=train_num]

    return {'daily_test_df':daily_test_df}


back_df=split_back_trader()['daily_test_df']
# print('日频测试切分：',back_df.shape)



backtrader_df=back_tes_trader.daily_test_data(back_df)

# print(backtrader_df.shape)
# print(backtrader_df)

backtrader_df['rate_of_return'] = backtrader_df['close'].rolling(2).apply(lambda x: x[1] / x[0] - 1, raw=True)
backtrader_df['day_rate_of_return']=backtrader_df['close']/backtrader_df['open']-1

clo_1=backtrader_df.loc[(backtrader_df.index<total_day-1),"close"].tolist()

backtrader_df.loc[(backtrader_df.index>=train_num+20+1),'last_close']=clo_1
backtrader_df['sale_rate_of_return']=backtrader_df['open']/backtrader_df['last_close']-1
# def get_backtrader_character(x):
#     if

# print(backtrader_df)
print(backtrader_df)
print(backtrader_df.shape)


def backtrader(list,df):
    trade_day_return_list = []
    return_list = []
    every_day_return_list = []
    a=0

    rate_of_return = 1
    for i,v in enumerate(list):
        if (v ==1)&(a==0):
            b=(1 + df.loc[train_num+20 + i, 'day_rate_of_return'])
            rate_of_return= rate_of_return * b
            a=1
            trade_day_return_list.append(b-1)
            return_list.append(rate_of_return)
            every_day_return_list.append(b - 1)


        elif (v ==1)&(a==1):
            b=(1 + df.loc[train_num+20 + i, 'rate_of_return'])
            rate_of_return= rate_of_return *b
            a=a
            trade_day_return_list.append(b-1)
            return_list.append(rate_of_return)
            every_day_return_list.append(b - 1)
        elif (v==0)&(a==0):
            rate_of_return=rate_of_return
            a=a
            every_day_return_list.append(0)

        elif (v==0)&(a==1):
            a=0
            b = (1 + df.loc[train_num+20 + i, 'sale_rate_of_return'])
            rate_of_return=rate_of_return*b
            trade_day_return_list.append(b-1)
            every_day_return_list.append(b - 1)
            return_list.append(rate_of_return)

    # for i,rate in enumerate(every_day_return_list):
    #
    #     zhishu_list = []
    #     num=1
    #     for zi_rate in every_day_return_list[:i]:
    #         return_rate = zi_rate + 1
    #         num=return_rate*num
    #         zhishu_list.append(return_rate * 4109.716)
    # print(every_day_return_list)
    return every_day_return_list


result1=backtrader(y_pred1,backtrader_df)
result=backtrader(y_pred,backtrader_df)
result2=backtrader(y_pred2,backtrader_df)
print(result)

print(result1)



def zhishushouyilv(list):
    a=4109.716
    zhishu_list=[]
    for i, v in enumerate(list):
        a=a*(v+1)
        zhishu_list.append(a)
    return zhishu_list



zhishu_result=zhishushouyilv(result)
print(zhishu_result)
zhishu_result1=zhishushouyilv(result1)
print(zhishu_result1)

zhishu_result2=zhishushouyilv(result2)
print(zhishu_result2)

# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Heiti TC'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
x = trade_time


plt.plot(x, zhishu_result, marker='s', ms=3, label="Proposed",c="r")
plt.plot(x, zhishu_result1, marker='*', ms=4, label="多尺度CNN-LSTM")

plt.plot(x, zhishu_result2, marker='o', ms=4, label="LSTM")

plt.plot(x, husen300, ms=4, label="沪深300指数",c="g")


plt.xticks(rotation=0)
# plt.xlabel("发布日期")
# plt.ylabel("y标签")
# plt.title("80小说网活跃度")
plt.legend(loc='best')
# 在折线图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
# for y in [y1, y2, y3]:
#     for x1, yy in zip(x, y):
#         plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=10, rotation=0)
plt.savefig("a.jpg")
plt.show()