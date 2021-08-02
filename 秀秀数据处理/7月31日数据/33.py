import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据'
df=pd.read_excel(os.path.join(path,'33.xlsx'),usecols=[0,1,2],header=None,skiprows=3,dtype=object,names=['证券代码','截止日期','第一大股东持股比率(%)'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])
s=df['第一大股东持股比率(%)'].diff()
df['差额']=s
def get_score(x):
    if x['差额']>0:
        return 100
    if x['差额']==0:
        return 75
    if x['差额']<0:
        return 50
df.loc[:,'分数']=df.apply(get_score,axis=1)
df.drop('差额',axis=1,inplace=True)
df1=df.loc[(df['截止日期']>=pd.to_datetime('2010-12-31'))&(df['截止日期']<=pd.to_datetime('2020-12-31'))]
print(df1)


df1.to_excel(os.path.join(path,'33-.xlsx'),index=False)