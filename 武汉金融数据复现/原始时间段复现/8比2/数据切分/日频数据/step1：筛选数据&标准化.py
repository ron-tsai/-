import pandas as pd
import os

path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始'

#日频数据处理
df1=pd.read_excel(os.path.join(path_dir,'step1：日频原数据拼接去重.xlsx'),dtype=object,col_index=False)
df1=df1.loc[:,~df1.columns.str.contains('Unnamed')]
df1['trade_time']=pd.to_datetime(df1['trade_time'])
df1.sort_values(by='trade_time',ascending=True,inplace=True)


total_df=df1.loc[(df1['trade_time']>=pd.to_datetime("2012-01-04"))&(df1['trade_time']<=pd.to_datetime("2019-09-30")),:]
total_df=total_df.loc[:,~total_df.columns.str.contains('Unnamed')]
s1=total_df.loc[(total_df['trade_time']>=pd.to_datetime('2012-01-04'))&(total_df['trade_time']<pd.to_datetime('2019-09-30')),'volume'].tolist()
print(len(s1))



total_df.loc[(total_df['trade_time']>=pd.to_datetime('2012-01-05'))&(total_df['trade_time']<=pd.to_datetime('2019-09-30')),'volume-1']=s1
total_df.loc[:,"volume_rate"]=total_df['volume']/total_df['volume-1']-1
total_df.drop(['volume','volume-1'],axis=1,inplace=True)
print(total_df)
#切割数据集
daily_train_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2012-01-05"))&(total_df['trade_time']<=pd.to_datetime("2018-02-21")),:]
print(daily_train_df)

# print(daily_val_df)
daily_test_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2018-02-22"))&(total_df['trade_time']<=pd.to_datetime("2019-09-27")),:]
print(daily_test_df)

##数据标准化
#训练集
train_open_mean_value = daily_train_df['open'].mean(axis=0)
train_high_mean_value = daily_train_df['high'].mean(axis=0)
train_low_mean_value = daily_train_df['low'].mean()
train_close_mean_value = daily_train_df['close'].mean()
train_volumerate_mean_value = daily_train_df['volume_rate'].mean()

train_open_std_value = daily_train_df['open'].std()
train_high_std_value = daily_train_df['high'].std()
train_low_std_value = daily_train_df['low'].std()
train_close_std_value = daily_train_df['close'].std()
train_volumerate_std_value = daily_train_df['volume_rate'].std()
#测试集
test_open_mean_value = daily_test_df['open'].mean(axis=0)
test_high_mean_value = daily_test_df['high'].mean(axis=0)
test_low_mean_value = daily_test_df['low'].mean()
test_close_mean_value = daily_test_df['close'].mean()
test_volumerate_mean_value = daily_test_df['volume_rate'].mean()

test_open_std_value = daily_test_df['open'].std()
test_high_std_value = daily_test_df['high'].std()
test_low_std_value = daily_test_df['low'].std()
test_close_std_value = daily_test_df['close'].std()
test_volumerate_std_value = daily_test_df['volume_rate'].std()

def train_norm(df):

    df['open']=(df['open']-train_open_mean_value)/train_open_std_value
    df['high'] = (df['high'] - train_high_mean_value) / train_high_std_value
    df['low'] =  (df['low'] - train_low_mean_value) / train_low_std_value
    df['close'] =  (df['close'] - train_close_mean_value) / train_close_std_value
    df['volume_rate'] = (df['volume_rate'] - train_volumerate_mean_value) / train_volumerate_std_value

    return df
train_norm=daily_train_df.apply(train_norm,axis=1)

def tes_norm(df):

    df['open']=(df['open']-test_open_mean_value)/test_open_std_value
    df['high'] = (df['high'] - test_high_mean_value) / test_high_std_value
    df['low'] =  (df['low'] - test_low_mean_value) / test_low_std_value
    df['close'] =  (df['close'] - test_close_mean_value) / test_close_std_value
    df['volume_rate'] = (df['volume_rate'] - test_volumerate_mean_value) / test_volumerate_std_value

    return df
test_norm=daily_test_df.apply(tes_norm,axis=1)
save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\\8比2\日频'
train_norm.to_excel(os.path.join(save_dir,'train_norm.xlsx'))
test_norm.to_excel(os.path.join(save_dir,'test_norm.xlsx'))

# print(daily_train_df,daily_test_df)