import pandas as pd
import numpy as np
val_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_val_data.xlsx')
target_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\每日涨跌数据\\验证集target.xlsx',index_col='trade_time',parse_dates=True)
# train_df['trade_time']=pd.to_datetime(train_df['trade_time'])


print(val_df.loc[val_df.index==320])
print(val_df)

rows=list(range(320,1600,16))

print(rows)
print(len(rows))

samples = np.zeros((len(rows),
                           16,
                           4))
targets=np.zeros((len(rows),))
for j, row in enumerate(rows):

    time_step=16

    samples[j] =val_df.loc[(val_df.index>=row-time_step) &(val_df.index < row),'open':]

    target_index=val_df.loc[(val_df.index==row),'trade_time'].dt.date.values[0]
    # target_index=target_index.values[0]
    target_index2=pd.to_datetime(target_index)

    # print(target_index)
    # print(target_index2)
    # print(target_df.loc[target_df.index == target_index2, 'target'])
    targets[j] = target_df.loc[target_df.index == target_index2, 'target']
    print(samples)