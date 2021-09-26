import pandas as pd
import os

path='F:\\newstart\software\category\\tool\category\deal_with_data\\1\合并数据'





df2=pd.read_excel(os.path.join(path,'666.xlsx'),dtype=object)
df0=pd.read_excel(os.path.join(path,'7.xlsx'),parse_dates=True)
df0.loc[:,'trade_time']=pd.to_datetime(df0['trade_time'])


df=pd.merge(df2,df0,on='trade_time',how='left')

df.to_excel(os.path.join(path,'666777.xlsx'),index=False)