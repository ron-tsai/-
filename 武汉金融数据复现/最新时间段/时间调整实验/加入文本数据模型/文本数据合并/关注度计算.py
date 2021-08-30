import pandas as pd
import os

path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'
df=pd.read_excel(os.path.join(path,'guanzhudu_data.xlsx'))
df.loc[:,'date'] = pd.to_datetime(df['date'])
df.set_index(df['date'],inplace=True)
df.drop('date',inplace=True,axis=1)
print(df)
df1=df.resample('W').mean()
# print(df1)
index_list=df.index
df2=df1.reindex(index_list,method='bfill')
# print(df2)
df['mean']=df2['search_index']

df['finish_search']=df['search_index']/df['mean']
print(df)
df.drop('mean',inplace=True,axis=1)
df.drop('search_index',inplace=True,axis=1)

sent_df=pd.read_excel(os.path.join(path,'合并.xlsx'),encoding='gbk')
df_merge=pd.merge(sent_df,df,on='date',how='outer')

df_wenben=df_merge.loc[(df_merge['date']>=pd.to_datetime('2013-01-09'))&(df_merge['date']<=pd.to_datetime('2021-07-02')),:]
print(df_wenben)
df_wenben.to_excel(os.path.join(path,'wenben86.xlsx'))