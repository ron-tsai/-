import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os

fif_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\8比1比1\\15分钟频数据'
fif_train_df=pd.read_excel(os.path.join(fif_dir,'fif_train_data.xlsx'))
fif_val_df=pd.read_excel(os.path.join(fif_dir,'fif_val_data.xlsx'))
fif_test_df=pd.read_excel(os.path.join(fif_dir,'fif_test_data.xlsx'))

daily_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\8比1比1\\日频数据'
daily_train_df=pd.read_excel(os.path.join(daily_dir,'daily_train_data.xlsx'))
daily_val_df=pd.read_excel(os.path.join(daily_dir,'daily_val_data.xlsx'))
daily_test_df=pd.read_excel(os.path.join(daily_dir,'daily_test_data.xlsx'))

target_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\8比1比1\涨跌目标数据'
train_target_df=pd.read_excel(os.path.join(target_dir,'训练集target.xlsx'))
val_target_df=pd.read_excel(os.path.join(target_dir,'验证集target.xlsx'))
test_target_df=pd.read_excel(os.path.join(target_dir,'测试集target.xlsx'))


print(daily_val_df['open'].mean(axis=0))
print(daily_val_df['open'].mean())
print(daily_val_df['open'].std(axis=0))
print(daily_val_df['open'].std())


daily_open_mean_value = daily_train_df['open'].mean(axis=0)
daily_high_mean_value = daily_train_df['high'].mean(axis=0)
daily_low_mean_value = daily_train_df['low'].mean()
daily_close_mean_value = daily_train_df['close'].mean()
daily_volumerate_mean_value = daily_train_df['volume_rate'].mean()

daily_open_std_value = daily_train_df['open'].std()
daily_high_std_value = daily_train_df['high'].std()
daily_low_std_value = daily_train_df['low'].std()
daily_close_std_value = daily_train_df['close'].std()
daily_volumerate_std_value = daily_train_df['volume_rate'].std()

fif_open_mean_value = fif_train_df['open'].mean(axis=0)
fif_high_mean_value = fif_train_df['high'].mean(axis=0)
fif_low_mean_value = fif_train_df['low'].mean()
fif_close_mean_value = fif_train_df['close'].mean()

fif_volumerate_mean_value = fif_train_df['volume_rate'].mean()

fif_open_std_value = fif_train_df['open'].std()
fif_high_std_value = fif_train_df['high'].std()
fif_low_std_value = fif_train_df['low'].std()
fif_close_std_value = fif_train_df['close'].std()
fif_volumerate_std_value = fif_train_df['volume_rate'].std()
def daily_norm(df):

    df['open']=(df['open']-daily_open_mean_value)/daily_open_std_value
    df['high'] = (df['high'] - daily_high_mean_value) / daily_high_std_value
    df['low'] =  (df['low'] - daily_low_mean_value) / daily_low_std_value
    df['close'] =  (df['close'] - daily_close_mean_value) / daily_close_std_value
    df['volume_rate'] = (df['volume_rate'] - daily_volumerate_mean_value) / daily_volumerate_std_value

    return df
def fif_norm(df):

    df['open']=(df['open']-fif_open_mean_value)/daily_open_std_value
    df['high'] = (df['high'] - fif_high_mean_value) / daily_high_std_value
    df['low'] =  (df['low'] - fif_low_mean_value) / daily_low_std_value
    df['close'] =  (df['close'] - fif_close_mean_value) / fif_close_std_value
    df['volume_rate'] = (df['volume_rate'] - fif_volumerate_mean_value) / fif_volumerate_std_value

    return df
daily_norm=daily_val_df.apply(daily_norm,axis=1)
fif_norm=fif_val_df.apply(fif_norm,axis=1)
print(daily_norm)
print(fif_norm)
fif_norm=fif_norm.loc[:,~fif_norm.columns.str.contains('Unnamed')]
daily_norm=daily_norm.loc[:,~daily_norm.columns.str.contains('Unnamed')]

fif_norm.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\8比1比1\标准化后数据\\fif_val_data.xlsx')
daily_norm.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\8比1比1\标准化后数据\\daily_val_data.xlsx')
