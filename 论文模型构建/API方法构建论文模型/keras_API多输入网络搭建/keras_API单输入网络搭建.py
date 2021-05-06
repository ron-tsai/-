from keras.models import Model
from keras import layers
from keras import Input
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# 15分钟频输入训练(!!!卷积滤镜行列先后)
fif_min_input=Input(shape=(16,4),dtype='float32',name='fif_min')
# fif_min_input=(8,16,4,1)
Conv1D_fif=layers.Conv1D(16,(1),strides=1)(fif_min_input)
LSTM_fif=layers.LSTM(100)(Conv1D_fif)

# 日频输入训练
##daily_input=Input(shape=(4,1),batch_shape=None,dtype='float32',name='daily')
# daily_input=(8,16,4,1)
##Conv1D_daily=layers.Conv1D(16,4,strides=1)(daily_input)
##LSTM_daily=layers.LSTM(100)(Conv1D_daily)
# 15分钟频训练结果和日频训练结果合并
##concatenated=layers.concatenate([LSTM_fif,LSTM_daily],axis=-1) # axis=-1按照最后一个轴粘合

alloy=layers.Dense(20,activation='relu')(LSTM_fif) #将粘合结果再接一个全连接层
output=layers.Dropout(0.5)(alloy)
model=Model(fif_min_input,output) #八股文：将输入和输出圈起来

print(model.summary())
model.compile(optimizer='rmsprop',loss='sparse_categorical_crossentropy',metrics=['acc'])


fif_train_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_train_data.xlsx')
fif_val_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_val_data.xlsx')
fif_test_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_test_data.xlsx')

daily_train_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\日频数据\daily_train_data.xlsx')
daily_val_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\日频数据\daily_val_data.xlsx')
daily_test_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\日频数据\daily_test_data.xlsx')

train_target_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\每日涨跌数据\\训练集target.xlsx',index_col='trade_time',parse_dates=True)
val_target_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\每日涨跌数据\\验证集target.xlsx',index_col='trade_time',parse_dates=True)
test_target_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\每日涨跌数据\\测试集target.xlsx',index_col='trade_time',parse_dates=True)




def generator(data,target_data,lookback,min_index,max_index
              ,time_step=16,variable=4,batch_size=32):

    i = min_index+lookback
    while 1:
        rows=list(range(i,max_index,time_step))
        samples = np.zeros((len(rows),
                           time_step,
                           variable))
        targets=np.zeros((len(rows),))
        for j,row in enumerate(rows):

            samples[j] = data.loc[(data.index >= row-time_step) & (data.index < row), 'open':]
            target_index = data.loc[(data.index == row), 'trade_time'].dt.date.values[0]
            # target_index=target_index.values[0]
            target_index2 = pd.to_datetime(target_index)


            targets[j] = target_data.loc[target_data.index == target_index2, 'target']
        yield samples,targets


##lookback是数据前蓝色区域的大小
##min_index从0开始，max_index为橙色+蓝色部分数据真实条数
fif_train_gen=generator(data=fif_train_df,target_data=train_target_df,lookback=320,
                        min_index=0,max_index=10560,time_step=16,batch_size=32)
fif_val_gen=generator(data=fif_val_df,target_data=val_target_df,lookback=320,
                        min_index=0,max_index=1600,time_step=16,batch_size=32)
fif_test_gen=generator(data=fif_test_df,target_data=test_target_df,lookback=320,
                        min_index=0,max_index=1600,time_step=16,batch_size=32)
daily_train_gen=generator(data=daily_train_df,target_data=train_target_df,lookback=20,
                          min_index=0,max_index=660,time_step=20,batch_size=32)
daily_val_gen=generator(data=daily_val_df,target_data=val_target_df,lookback=20,
                          min_index=0,max_index=100,time_step=20,batch_size=32)
daily_test_gen=generator(data=daily_test_df,target_data=test_target_df,lookback=20,
                          min_index=0,max_index=100,time_step=20,batch_size=32)


print(fif_train_gen)
history=model.fit_generator(fif_train_gen,steps_per_epoch=10,epochs=100,
                            )




