import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'
df=pd.read_excel(os.path.join(path,'公司年龄 .xlsx'),usecols=[0,1,2,3],header=None,skiprows=3,dtype=object,names=['证券代码','股票简称','截止日期','成立日期'])

df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])
df.loc[:,'成立日期']=pd.to_datetime(df['成立日期'])


def get_time(x):
    if x['成立日期']:
        return (x['截止日期'] - x['成立日期'])/pd.Timedelta(days=365)

df.loc[:,'公司年龄']=df.apply(get_time,axis=1)
df.loc[:,'公司年龄']=df['公司年龄'].fillna(0)
df['公司年龄'] = [int(y)+1 for y in df['公司年龄']]
df.to_excel(os.path.join(path,'gongsinianling.xlsx'),index=False)