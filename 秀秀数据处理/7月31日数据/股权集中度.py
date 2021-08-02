

import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据'
df=pd.read_excel(os.path.join(path,'股权集中度.xlsx'),usecols=[0,1,2],header=None,skiprows=3,dtype=object,names=['证券代码','截止日期','第一大股东持股比例'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期']).dt.date
df['截止月份']=pd.to_datetime(df['截止日期']).dt.month

df=df.loc[df['截止月份']==12]
df.drop('截止月份',axis=1,inplace=True)




df.to_excel(os.path.join(path,'股权集中度-.xlsx'),index=False)