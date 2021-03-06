from keras.models import Model
from keras import layers
from keras import Input
from keras import optimizers
from keras import regularizers
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os

##### 一、模型搭建
# 15分钟频输入训练(!!!卷积滤镜行列先后)
fif_min_input=Input(shape=(16,5),dtype='float32',name='fif_min_input')
# fif_min_input=(8,16,4,1)
Conv1D_fif=layers.Conv1D(16,1,strides=1)(fif_min_input)
LSTM_fif=layers.LSTM(100,activation='relu',recurrent_dropout=0.2)(Conv1D_fif)

# 日频输入训练
daily_input=Input(shape=(20,5),dtype='float32',name='daily_input')
# daily_input=(8,16,4,1)
Conv1D_daily=layers.Conv1D(16,1,strides=1)(daily_input)
LSTM_daily=layers.LSTM(100,activation='relu',recurrent_dropout=0.2)(Conv1D_daily)
# 15分钟频训练结果和日频训练结果合并
concatenated=layers.concatenate([LSTM_fif,LSTM_daily],axis=-1) # axis=-1按照最后一个轴粘合

alloy=layers.Dense(20,activation='relu')(concatenated) #将粘合结果再接一个全连接层
dropout=layers.Dropout(0.5)(alloy)
output=layers.Dense(1,activation='sigmoid')(dropout)
model=Model([fif_min_input,daily_input],output) #八股文：将输入和输出圈起来

print(model.summary())
model.compile(optimizer=optimizers.Adam(lr=0.001),loss='binary_crossentropy',metrics=['mse','acc'])

##### 二、数据导入
finally_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\8比1比1\标准化后数据'

fif_train_df=pd.read_excel(os.path.join(finally_dir,'fif_train_data.xlsx'))
fif_val_df=pd.read_excel(os.path.join(finally_dir,'fif_val_data.xlsx'))
fif_test_df=pd.read_excel(os.path.join(finally_dir,'fif_test_data.xlsx'))

daily_train_df=pd.read_excel(os.path.join(finally_dir,'daily_train_data.xlsx'))
daily_val_df=pd.read_excel(os.path.join(finally_dir,'daily_val_data.xlsx'))
daily_test_df=pd.read_excel(os.path.join(finally_dir,'daily_test_data.xlsx'))

target_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\8比1比1\涨跌目标数据'
train_target_df=pd.read_excel(os.path.join(target_dir,'训练集target.xlsx'))
val_target_df=pd.read_excel(os.path.join(target_dir,'验证集target.xlsx'))
test_target_df=pd.read_excel(os.path.join(target_dir,'测试集target.xlsx'))



def generator(input_data1,input_data2,target_data):
    while 1:
        rows = list(range(1, 1681))
        samples1 = np.zeros((len(rows),
                             16,
                             5))
        samples2 = np.zeros((len(rows),
                             20,
                             5))

        targets = np.zeros((len(rows),))

        for j in rows:
            samples1[j - 1] = input_data1.loc[
                              (input_data1.index >= 320 + j * 16 - 32) & (input_data1.index < 320 + j * 16 - 16),
                              'open':]
            samples2[j - 1] = input_data2.loc[
                              (input_data2.index >= j -1) & (input_data2.index < 20 + j - 1),
                              'open':]

            targets[j - 1] = target_data.loc[target_data.index == j - 1, 'target']
        yield ({'fif_min_input': samples1, 'daily_input': samples2}, targets)


train_gen=generator(fif_train_df,daily_train_df,train_target_df)


def val_tes_generator(input_data1,input_data2,target_data):
    while 1:
        rows = list(range(1, 211))
        samples1 = np.zeros((len(rows),
                             16,
                             5))
        samples2 = np.zeros((len(rows),
                             20,
                             5))

        targets = np.zeros((len(rows),))

        for j in rows:
            samples1[j - 1] = input_data1.loc[
                              (input_data1.index >= 320 + j * 16 - 32) & (input_data1.index < 320 + j * 16 - 16),
                              'open':]
            samples2[j - 1] = input_data2.loc[
                              (input_data2.index >= j -1) & (input_data2.index < 20 + j - 1),
                              'open':]

            targets[j - 1] = target_data.loc[target_data.index == j - 1, 'target']
        return ([samples1,samples2],targets)

val_gen=val_tes_generator(fif_val_df,daily_val_df,val_target_df)
# print(val_gen)
history=model.fit_generator(generator=train_gen,validation_steps=5,steps_per_epoch=2,validation_data=val_gen,epochs=300)

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
plt.show()
