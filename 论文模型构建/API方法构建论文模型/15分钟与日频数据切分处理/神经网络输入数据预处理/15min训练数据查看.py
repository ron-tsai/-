import pandas as pd
import numpy as np
train_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_train_data.xlsx')
target_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\每日涨跌数据\\训练集target.xlsx',index_col='trade_time',parse_dates=True)
# train_df['trade_time']=pd.to_datetime(train_df['trade_time'])


print(train_df.loc[train_df.index==320])


rows=list(range(320,10560,16))

print(rows)
print(len(rows))

samples = np.zeros((len(rows),
                           16,
                           4))
targets=np.zeros((len(rows),))
for j, row in enumerate(rows):

    time_step=16

    samples[j] =train_df.loc[(train_df.index>=row-time_step) &(train_df.index < row),'open':]

    target_index=train_df.loc[(train_df.index==row),'trade_time'].dt.date.values[0]
    # target_index=target_index.values[0]
    target_index2=pd.to_datetime(target_index)

    # print(target_index)
    # print(target_index2)
    # print(target_df.loc[target_df.index == target_index2, 'target'])
    targets[j] = target_df.loc[target_df.index == target_index2, 'target']
    print(samples)