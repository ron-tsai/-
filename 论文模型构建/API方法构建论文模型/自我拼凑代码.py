from keras.models import Model
from keras import layers
from keras import Input
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# 15分钟频输入训练(!!!卷积滤镜行列先后)
fif_min_input=Input(shape=(4,1),dtype='float32',name='fif_min')
# fif_min_input=(8,16,4,1)
Conv1D_fif=layers.Conv1D(16,4,strides=1)(fif_min_input)
LSTM_fif=layers.LSTM(100)(Conv1D_fif)

# 日频输入训练
daily_input=Input(shape=(4,1),batch_shape=None,dtype='float32',name='daily')
# daily_input=(8,16,4,1)
Conv1D_daily=layers.Conv1D(16,4,strides=1)(daily_input)
LSTM_daily=layers.LSTM(100)(Conv1D_daily)
# 15分钟频训练结果和日频训练结果合并
concatenated=layers.concatenate([LSTM_fif,LSTM_daily],axis=-1) # axis=-1按照最后一个轴粘合

alloy=layers.Dense(20,activation='relu')(concatenated) #将粘合结果再接一个全连接层
output=layers.Dropout(0.5)(alloy)
model=Model([fif_min_input,daily_input],output) #八股文：将输入和输出圈起来

print(model.summary())
model.compile(optimizer='rmsprop',loss='sparse_categorical_crossentropy',metrics=['acc'])


fif_train_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_train_data.xlsx')
daily_train_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\日频数据\daily_train_data.xlsx')

fif_validation_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_val_data.xlsx')
daily_validatioin_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\日频数据\daily_val_data.xlsx')
target_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\每日涨跌数据\\训练集target.xlsx',index_col='trade_time',parse_dates=True)



def generator(train_or_val_data,target_data,lookback,delay,min_index,max_index,
              suffle=False,time_step,variable=4,batch_size=128,step=6):

    i = min_index+lookback
    while 1:
        if shuffle:  ##训练资料使用
            rows=list(range(i,max_index,16))
        else:
            if i + batch_size >= max_index:
                i += len(rows)
            rows=np.average(i,min(i+batch_size,max_index))
            i+=len(rows)
        samples = np.zeros((len(rows),
                           time_step,
                           variable))
        targets=np.zeros((len(rows),))
        for j,row in enumerate(rows):

            samples[j] = train_or_val_data.loc[(train_or_val_data.index >= row-time_step) & (train_data.index < row), 'open':]
            target_index = train_or_val_data.loc[(train_or_val_data.index == row), 'trade_time'].dt.date.values[0]
            # target_index=target_index.values[0]
            target_index2 = pd.to_datetime(target_index)


            targets[j] = target_df.loc[target_df.index == target_index2, 'target']
        yield samples,targets

fif_train_min_index=0
fif_train_max_index=10559
fif_train_look_back=320


history=model.fit_generator(train_generator,steps_per_epoch=100,epochs=100,
                            validation_data=validation_generator,
                            validation_steps=50)




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


