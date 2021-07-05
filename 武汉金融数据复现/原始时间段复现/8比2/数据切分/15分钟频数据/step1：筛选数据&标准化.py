import pandas as pd
import os
import numpy as np

path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始'

#15分钟频数据处理
df1=pd.read_csv(os.path.join(path_dir,'沪深300-15min.csv'),dtype=object,usecols=['trade_time','open','close','high','low','volume'])

df1=df1.loc[:,~df1.columns.str.contains('Unnamed')]
df1['trade_time']=pd.to_datetime(df1['trade_time'])
df1.sort_values(by='trade_time',ascending=True,inplace=True)


total_df=df1.loc[(df1['trade_time']>=pd.to_datetime("2012-01-04 15:00:00"))&(df1['trade_time']<=pd.to_datetime("2019-09-27 15:00:00")),:]
total_df=total_df.loc[:,~total_df.columns.str.contains('Unnamed')]
# print(total_df)
s1=total_df.loc[(total_df['trade_time']>=pd.to_datetime('2012-01-04 15:00:00'))&(total_df['trade_time']<pd.to_datetime('2019-09-27 15:00:00')),'volume'].tolist()
# print(total_df.loc[(total_df['trade_time']>=pd.to_datetime('2012-01-04 15:00:00'))&(total_df['trade_time']<pd.to_datetime('2019-09-27 15:00:00')),])
# print(len(s1))



total_df.loc[(total_df['trade_time']>=pd.to_datetime('2012-01-05 9:45:00'))&(total_df['trade_time']<=pd.to_datetime('2019-09-27 15:00:00')),'volume-1']=s1
# print(total_df)
total_df['volume'] = total_df['volume'].astype(np.float64)
total_df['volume-1'] = total_df['volume-1'].astype(np.float64)
total_df['open'] = total_df['open'].astype(np.float64)
total_df['close'] = total_df['close'].astype(np.float64)
total_df['high'] = total_df['high'].astype(np.float64)
total_df['low'] = total_df['low'].astype(np.float64)

# total_df['volume'] = pd.to_numeric(total_df['volume'],errors='coerce')
# total_df['volume-1'] = pd.to_numeric(total_df['volume-1'],errors='coerce')
def v_rate(x):
    if x['volume']==0:
        return 0
    if x['volume-1']==0:
        return 0
    else:
        return x['volume']/x['volume-1']-1
total_df.loc[:, "volume_rate"] = total_df.apply(v_rate,axis=1)
# total_df.loc[:,"volume_rate"]=total_df['volume']/total_df['volume-1']-1
total_df.drop(['volume','volume-1'],axis=1,inplace=True)
# print(total_df["volume_rate"])
# print(total_df)
#切割数据集
fif_train_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2012-01-05 9:45:00"))&(total_df['trade_time']<=pd.to_datetime("2018-02-21 15:00:00")),:]
# print(fif_train_df)

# print(daily_val_df)
fif_test_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2018-02-22 9:45:00"))&(total_df['trade_time']<=pd.to_datetime("2019-09-27 15:00:00")),:]
# print(fif_test_df)

##数据标准化
#训练集
train_open_mean_value = fif_train_df['open'].mean(axis=0)
train_high_mean_value = fif_train_df['high'].mean(axis=0)
train_low_mean_value = fif_train_df['low'].mean()
train_close_mean_value = fif_train_df['close'].mean()
train_volumerate_mean_value = fif_train_df['volume_rate'].mean()
print(train_volumerate_mean_value)

train_open_std_value = fif_train_df['open'].std()
train_high_std_value = fif_train_df['high'].std()
train_low_std_value = fif_train_df['low'].std()
train_close_std_value = fif_train_df['close'].std()
train_volumerate_std_value = fif_train_df['volume_rate'].std()
###关键点
# fif_train_df[['open','volume_rate']].to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\8比2\排查.xlsx')
print(train_volumerate_std_value)
#测试集
test_open_mean_value = fif_test_df['open'].mean(axis=0)
test_high_mean_value = fif_test_df['high'].mean(axis=0)
test_low_mean_value = fif_test_df['low'].mean()
test_close_mean_value = fif_test_df['close'].mean()
test_volumerate_mean_value = fif_test_df['volume_rate'].mean()

test_open_std_value = fif_test_df['open'].std()
test_high_std_value = fif_test_df['high'].std()
test_low_std_value = fif_test_df['low'].std()
test_close_std_value = fif_test_df['close'].std()
test_volumerate_std_value = fif_test_df['volume_rate'].std()

def train_norm(df):

    df['open']=(df['open']-train_open_mean_value)/train_open_std_value
    df['high'] = (df['high'] - train_high_mean_value) / train_high_std_value
    df['low'] =  (df['low'] - train_low_mean_value) / train_low_std_value
    df['close'] =  (df['close'] - train_close_mean_value) / train_close_std_value
    df['volume_rate'] = (df['volume_rate'] - train_volumerate_mean_value) / train_volumerate_std_value

    return df
train_norm=fif_train_df.apply(train_norm,axis=1)

def tes_norm(df):

    df['open']=(df['open']-test_open_mean_value)/test_open_std_value
    df['high'] = (df['high'] - test_high_mean_value) / test_high_std_value
    df['low'] =  (df['low'] - test_low_mean_value) / test_low_std_value
    df['close'] =  (df['close'] - test_close_mean_value) / test_close_std_value
    df['volume_rate'] = (df['volume_rate'] - test_volumerate_mean_value) / test_volumerate_std_value

    return df
test_norm=fif_test_df.apply(tes_norm,axis=1)
save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\\8比2\\15分钟频'
print(train_norm,test_norm)
train_norm.to_excel(os.path.join(save_dir,'train_norm.xlsx'))
test_norm.to_excel(os.path.join(save_dir,'test_norm.xlsx'))

