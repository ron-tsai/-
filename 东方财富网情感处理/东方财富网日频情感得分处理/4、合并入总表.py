import pandas as pd
import os

path='/Users/ccmac/Desktop/情感分析存储'
new_dir='/Users/ccmac/Documents/毕业论文数据/数据二合为一'


mix_file='777888.xlsx'
df0 = pd.read_excel(os.path.join(path, '年情感分析总表.xlsx'), dtype=object)
df0.sort_values(by='trade_time')
df0.loc[:, 'trade_time'] = pd.to_datetime(df0['trade_time']).dt.date

wenben_df=pd.read_excel(os.path.join(new_dir,mix_file))

begin_date='2016-01-01'
end_date='2021-09-30'


begin=pd.to_datetime(begin_date)
end=pd.to_datetime(end_date)

wenben_df=wenben_df.loc[(wenben_df['trade_time']>=begin)&(wenben_df['trade_time']<=end),:].reset_index()
wenben_df.loc[:, 'trade_time'] = pd.to_datetime(wenben_df['trade_time']).dt.date


df2 = pd.merge(wenben_df,df0,on='trade_time',how='left')
df2.to_excel(os.path.join(path,'加入东方财富网股吧评论数据777888.xlsx'),index=False)

