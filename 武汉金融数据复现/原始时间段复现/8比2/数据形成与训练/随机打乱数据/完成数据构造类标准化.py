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
    def __init__(self,train_num,test_num,fif_back,daily_back):
        self.train_num=train_num
        self.test_num=test_num
        self.fif_back=fif_back
        self.daily_back=daily_back

    def daily_train_data(self,data):
        while True:
            rows = list(range(self.train_num - self.daily_back)) #总共1489个数据，由于扣除前面20个数据，所以为1469
            samples = np.zeros((len(rows),
                                 self.daily_back,
                                 5))
            for j in rows:

                samples[j] = data.loc[
                                  (data.index >= j) & (data.index < self.daily_back + j),
                                  'open':]
            return samples
    def fif_train_data(self,data):
        while True:
            rows = list(range(self.train_num - self.daily_back))
            samples = np.zeros((len(rows),
                                 self.fif_back,
                                 5))
            for j in rows:

                samples[j] = data.loc[
                              (data.index >= j * self.fif_back ) & (data.index < (j+1) * self.fif_back),
                              'open':]
            return samples

    def daily_test_data(self,data):
        while True:
            rows = list(range(self.test_num - self.daily_back))
            samples = np.zeros((len(rows),
                                self.daily_back,
                                 5))
            for j in rows:

                samples[j] = data.loc[
                                  (data.index >= j) & (data.index < self.daily_back + j),
                                  'open':]
            return samples
    def fif_test_data(self,data):
        while True:
            rows = list(range(self.test_num - self.daily_back))
            samples = np.zeros((len(rows),
                                self.fif_back,
                                 5))
            for j in rows:

                samples[j] = data.loc[
                                 (data.index >= (j) * self.fif_back) & (data.index < (j+1) * self.fif_back),
                                 'open':]
            return samples
    def target_train_data(self,data):
        while True:
            rows = list(range(self.train_num-self.daily_back))
            targets = np.zeros((len(rows),))
            for j in rows:
                targets[j] = data.loc[data.index == j, 'target']
            return targets
    def target_test_data(self,data):
        while True:
            rows = list(range(self.test_num-self.daily_back))
            targets = np.zeros((len(rows),))
            for j in rows:
                targets[j] = data.loc[data.index == j, 'target']
            return targets


origin_data=Data_maker(train_num=1489,test_num=393,fif_back=16,daily_back=20)
fif_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\\8比2\\15分钟频'
daily_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\\8比2\日频'
target_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\\8比2\每日涨跌'
daily_train_df=pd.read_excel(os.path.join(daily_dir,'train_norm.xlsx'))
fif_train_df=pd.read_excel(os.path.join(fif_dir,'train_norm.xlsx'))
daily_test_df=pd.read_excel(os.path.join(daily_dir,'test_norm.xlsx'))
fif_test_df=pd.read_excel(os.path.join(fif_dir,'test_norm.xlsx'))
target_train_df=pd.read_excel(os.path.join(target_dir,'test_target.xlsx'))
target_test_df=pd.read_excel(os.path.join(target_dir,'test_target.xlsx'))
DM=origin_data

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


def shuffle_data(fif_data,daily_data,target):

    a = list(range(1469))
    shuffle_list = np.random.choice(a, 1096, replace=False)
    rows = list(range(0, 1469)) #总共1489个数据，由于扣除前面20个数据，所以为1469
    val_list = list(set(rows)-set(shuffle_list))
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

    for i,v in enumerate(shuffle_list):

        fif_train_samples[i] = fif_data[v]
        daily_train_samples[i] = daily_data[v]
        train_targets[i] = target[v]
    for i,v in enumerate(val_list):
        daily_val_samples[i] = daily_data[v]
        fif_val_samples[i] = fif_data[v]
        val_targets[i] = target[v]


    return {'fif_train_samples':fif_train_samples,
            'daily_train_samples':daily_train_samples,
            'train_targets':train_targets,
            'fif_val_samples':fif_val_samples,
            'daily_val_samples':daily_val_samples,
            'val_targets':val_targets}

data=shuffle_data(fif_train,daily_train,target_train)

fif_train=data.get('fif_train_samples')
daily_train=data.get('daily_train_samples')
daily_val=data.get('daily_val_samples')
fif_val=data.get('fif_val_samples')
val_targets=data.get('val_targets')
train_targets=data.get('train_targets')


def my_model():
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
    model.compile(optimizer=keras.optimizers.adam(lr=1e-5),loss='binary_crossentropy',metrics=['acc'])
    return model
    # reduce_lr = ReduceLROnPlateau(monitor='val_loss', patience=5, mode='auto')

model=my_model()

history=model.fit(x=[fif_train,daily_train],y=train_targets,batch_size=32,validation_data=([fif_val,daily_val],val_targets),epochs=200)

# model.save("10.model")
loss,accuracy = model.evaluate(x=[fif_test,daily_test],y=target_test)

print(loss,accuracy)
def paint():
    acc=history.history['acc']
    val_acc=history.history['val_acc']
    loss=history.history['loss']
    val_loss=history.history['val_loss']

    epochs=range(len(acc))
    plt.plot(epochs,acc,'bo',label='Training acc')
    plt.plot(epochs,val_acc,'b',label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()

    plt.figure()

    plt.plot(epochs,loss,'bo',label='Training loss')
    plt.plot(epochs,val_loss,'b',label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    return plt
my_paint=paint()
my_paint.show()

