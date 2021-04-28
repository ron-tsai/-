from keras.layers import LSTM
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def generator(data,lookback,delay,min_index,max_index,
              suffle=False,batch_size=128,step=6):
    if max_index is None:
        max_index=len(data)-delay-1
    i = min_index+lookback
    while 1:
        if shuffle:
            rows=np.random.randint(
                min_index+lookback,max_index,size=batch_size)
        else:
            if i + batch_size >= max_index:
                i += len(rows)
            rows=np.average(i,min(i+batch_size,max_index))
            i+=len(rows)
        samples = np.zeros((len(rows),
                           lookback // step,
                           data.shape[-1]))
        targets=np.zeros((len(rows),))
        for j,row in enumerate(rows):
            indices=range(rows[j]-lookback,rows[j],step)
            samples[j]=data[indices]
            targets[j]=data[rows[j]+delay][1]
        yield samples,targets


lookback=720
step=6
delay=144
batch_size=128
data_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据'
min_fif_path=os.path.join(data_dir,'沪深300-15min.csv')
daily_path=os.path.join(data_dir,'沪深300日频数据.xlsx')


min_fif_data=pd.read_csv(min_fif_path,index_col='trade_time',parse_dates=True)
min_fif_data=min_fif_data.loc['2017-03-06':]
print(min_fif_data)
min_fif_train_data=min_fif_data[:'2020-03-31']

print(min_fif_train_data)
min_fif_val_data=min_fif_data['2020-04-01':'2020-9-30']
print(min_fif_val_data)
min_fif_test_data=min_fif_data['2020-10-08':]
print(min_fif_test_data)
close_price=min_fif_data['close']
date=min_fif_data.index
plt.plot(date,close_price)
plt.show()


min_fif_train_gen=generator(min_fif_data,
                    lookback=lookback,
                    delay=delay,
                    min_index=0,
                    max_index=200000,
                    shuffle=True,
                    step=step,
                    batch_size=batch_size)
min_fif_val_gen=generator(min_fif_data,
                  lookback=lookback,
                  delay=delay,
                  min_index=200001,
                  max_index=300000,
                  step=step,
                  batch_size=batch_size)
min_fif_test_gen=generator(min_fif_data,
                   lookback=lookback,
                   delay=delay,
                   min_index=300001,
                   max_index=None,
                   step=step,
                   batch_size=batch_size)

daily_train_gen=generator(daily_data,
                    lookback=lookback,
                    delay=delay,
                    min_index=0,
                    max_index=200000,
                    shuffle=True,
                    step=step,
                    batch_size=batch_size)
daily_val_gen=generator(daily_data,
                  lookback=lookback,
                  delay=delay,
                  min_index=200001,
                  max_index=300000,
                  step=step,
                  batch_size=batch_size)
daily_test_gen=generator(daily_data,
                   lookback=lookback,
                   delay=delay,
                   min_index=300001,
                   max_index=None,
                   step=step,
                   batch_size=batch_size)

