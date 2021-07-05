from numpy import random
# a=list(random.randint(0,100,4))
# print(a)
# b=list(range(100))
# print(b)
#
# # print(np.array([1234,233,234,2344]).slice(list(0,3)))
#
#
# c = list(set(b)-set(a))
# print(c)



import numpy as np
import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import sklearn
from keras.models import Model
from keras import layers
from keras import Input
from keras import callbacks
from keras.callbacks import ReduceLROnPlateau
import keras
from collections import Counter
import keras.losses

class Data_maker:
    def daily_train_data(self,data):
        while True:
            rows = list(range(1, 1470)) #总共1489个数据，由于扣除前面20个数据，所以为1469
            samples = np.zeros((len(rows),
                                 20,
                                 5))
            for j in rows:

                samples[j - 1] = data.loc[
                                  (data.index >= j -1) & (data.index < 20 + j -1),
                                  'open':]
            return samples
    def fif_train_data(self,data):
        while True:
            rows = list(range(1, 1470))
            samples = np.zeros((len(rows),
                                 16,
                                 5))
            for j in rows:

                samples[j - 1] = data.loc[
                              (data.index >= (j-1) * 16 ) & (data.index < j * 16),
                              'open':]
            return samples

    def daily_test_data(self,data):
        while True:
            rows = list(range(1, 374))
            samples = np.zeros((len(rows),
                                 20,
                                 5))
            for j in rows:

                samples[j - 1] = data.loc[
                                  (data.index >= j -1) & (data.index < 20 + j -1),
                                  'open':]
            return samples
    def fif_test_data(self,data):
        while True:
            rows = list(range(1, 374))
            samples = np.zeros((len(rows),
                                 16,
                                 5))
            for j in rows:

                samples[j - 1] = data.loc[
                                 (data.index >= (j - 1) * 16) & (data.index < j * 16),
                                 'open':]
            return samples
    def target_train_data(self,data):
        while True:
            rows = list(range(1, 1470))
            targets = np.zeros((len(rows),))
            for j in rows:
                targets[j - 1] = data.loc[data.index == j - 1, 'target']
            return targets
    def target_test_data(self,data):
        while True:
            rows = list(range(1, 374))
            targets = np.zeros((len(rows),))
            for j in rows:
                targets[j - 1] = data.loc[data.index == j - 1, 'target']
            return targets



fif_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\\8比2\\15分钟频'
daily_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\\8比2\日频'
target_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\\8比2\每日涨跌'
daily_train_df=pd.read_excel(os.path.join(daily_dir,'train_norm.xlsx'))
fif_train_df=pd.read_excel(os.path.join(fif_dir,'train_norm.xlsx'))
daily_test_df=pd.read_excel(os.path.join(daily_dir,'test_norm.xlsx'))
fif_test_df=pd.read_excel(os.path.join(fif_dir,'test_norm.xlsx'))
target_train_df=pd.read_excel(os.path.join(target_dir,'test_target.xlsx'))
target_test_df=pd.read_excel(os.path.join(target_dir,'test_target.xlsx'))
DM=Data_maker()

daily_train=DM.daily_train_data(daily_train_df)
daily_test=DM.daily_test_data(daily_test_df)
fif_train=DM.fif_train_data(fif_train_df)
fif_test=DM.fif_test_data(fif_test_df)
target_train=DM.target_train_data(target_train_df)
target_test=DM.target_test_data(target_test_df)
from numpy import random
# a=list(random.randint(0,100,4))
# print(a)
# b=list(range(100))
# print(b)
# print([random.randint(0,1469,4)])
# # print(np.array([1234,233,234,2344]).slice(list(0,3)))
# c=[]
# for i in a:
#     c.append(daily_train[i])
#     print(c)




a=list(range(1469))
shuffle_list=np.random.choice(a,1096,replace=False)
print(len(shuffle_list))
rows = list(range(0, 1469)) #总共1489个数据，由于扣除前面20个数据，所以为1469
val_list = list(set(rows)-set(shuffle_list))
print(len(val_list))
daily_train_samples = np.zeros((len(shuffle_list),
                     20,
                     5))
fif_train_samples = np.zeros((len(shuffle_list),
                    16,
                    5))
daily_val_samples = np.zeros((1469-len(shuffle_list),
                                20,
                                5))
fif_val_samples = np.zeros((1469-len(shuffle_list),
                              16,
                              5))
train_targets = np.zeros((1096,))
val_targets = np.zeros((373,))
print(val_targets.shape)

for i,v in enumerate(shuffle_list):
    print(i,v)
    fif_train_samples[i] = fif_train[v]
    daily_train_samples[i] = daily_train[v]
    train_targets[i] = target_train[v]
for i,v in enumerate(val_list):
    print(i,v)
    daily_val_samples[i] = daily_train[v]
    fif_val_samples[i] = fif_train[v]
    val_targets[i] = target_train[v]

print(daily_val_samples)
# return {'fif_train_samples':fif_train_samples,
#         'daily_train_samples':daily_train_samples,
#         'train_targets':train_targets,
#         'fif_val_samples':fif_val_samples,
#         'daily_val_samples':daily_val_samples,
#         'val_targets':val_targets}
#
# data=shuffle_data(fif_train,daily_train,target_train)
# print(data.get('daily_train_samples'))