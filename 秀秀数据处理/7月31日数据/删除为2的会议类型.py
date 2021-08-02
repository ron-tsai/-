import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据'
df=pd.read_excel(os.path.join(path,'1 .xlsx'),usecols=[0,1,2,3],header=None,skiprows=3,dtype=object,names=['证券代码','截止日期','报表类型','股东大会出席股份比例(%)'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])
df1=df.loc[(df['报表类型']==1)&(df['截止日期']>pd.to_datetime('2010-01-01'))&(df['截止日期']<pd.to_datetime('2020-12-31')),:]
df1.to_excel(os.path.join(path,'1-.xlsx'),index=False)