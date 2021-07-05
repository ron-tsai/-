import pandas as pd
import os
from matplotlib import pyplot as plt
import sklearn
from keras.models import Model
from keras import layers
from keras import Input
from keras import callbacks
from keras.callbacks import ReduceLROnPlateau
import keras
import keras.losses

import numpy as np

from keras.models import load_model
# load model from single file
model = load_model('10.model')


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

# np.set_printoptions(threshold='nan')


##### 一、模型搭建
# 15分钟频输入训练(!!!卷积滤镜行列先后)
fif_min_input=Input(shape=(16,5),dtype='float32',name='fif_min_input')
# fif_min_input=(8,16,4,1)
Conv1D_fif=layers.Conv1D(16,1,strides=1)(fif_min_input)
LSTM_fif=layers.LSTM(100)(Conv1D_fif)

# 日频输入训练
daily_input=Input(shape=(20,5),dtype='float32',name='daily_input')
# daily_input=(8,16,4,1)
Conv1D_daily=layers.Conv1D(16,1,strides=1)(daily_input)
LSTM_daily=layers.LSTM(100)(Conv1D_daily)
# 15分钟频训练结果和日频训练结果合并
concatenated=layers.concatenate([LSTM_fif,LSTM_daily],axis=-1) # axis=-1按照最后一个轴粘合

alloy=layers.Dense(20,activation='relu')(concatenated) #将粘合结果再接一个全连接层
dropout=layers.Dropout(0.2)(alloy)
output=layers.Dense(1,activation='sigmoid')(dropout)
model=Model([fif_min_input,daily_input],output) #八股文：将输入和输出圈起来

print(model.summary())
model.compile(optimizer=keras.optimizers.adam(lr=1e-4),loss='binary_crossentropy',metrics=['acc'])

reduce_lr = ReduceLROnPlateau(monitor='val_loss', patience=5, mode='auto')

# callbacks=[callbacks.EarlyStopping(monitor='val_loss',patience=0,verbose=0,mode='auto')]

# history=model.fit(x=[fif_train,daily_train],y=target_train,batch_size=32,validation_split=0.2,epochs=50,callbacks=[reduce_lr])
loss,accuracy = model.evaluate(x=[fif_test,daily_test],y=target_test)

print(loss,accuracy)




