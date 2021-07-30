# -*- coding: utf-8 -*-
__author__ = 'Cai Rong'
import pandas as pd
import os
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'
sent_df=pd.read_excel(os.path.join(path,'合并.xlsx'),encoding='gbk')
sent_df.loc[:,'date']=pd.to_datetime(sent_df['date'])
sent_df=sent_df.loc[:,~sent_df.columns.str.contains('Unnamed')]
sent_df.set_index(['date'],drop=True,inplace=True)

print(sent_df)
hushen_df=pd.read_csv(os.path.join(path,'沪深300.csv'),usecols=[3,4],encoding='gbk',skiprows=1,names=['date','search_index'])

hushen_df.loc[:,'date']=pd.to_datetime(hushen_df['date'])

hushen_df.set_index(['date'],drop=True,inplace=True)
print(hushen_df)
# print(hushen_df)
hus_df=hushen_df.loc[(hushen_df.index>=pd.to_datetime('2013-01-09'))&(hushen_df.index<=pd.to_datetime('2021-07-02')),:]
print(hus_df)
sent_df.reset_index(inplace=True)
hus_df.reset_index(inplace=True)
df=pd.merge(sent_df,hus_df,on='date',how='outer')
df=df.loc[:,~df.columns.str.contains('Unnamed')]
df1=df.loc[(df['date']>=pd.to_datetime('2013-01-09'))&(df['date']<=pd.to_datetime('2021-07-02')),:]
df1=df.loc[:,~df1.columns.str.contains('Unnamed')]
df1.dropna(axis=0,inplace=True)
print(df1)
df1.to_excel(os.path.join(path,'wenben_data.xlsx'))