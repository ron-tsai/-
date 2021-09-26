import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'
path1='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5\控制变量合并'
df=pd.read_excel(os.path.join(path,'gongsinianling.xlsx'),dtype=object)
df1=pd.read_excel(os.path.join(path1,'添加时间控制变量.xlsx'),dtype=object)
print(df1)

df1.loc[:,'截止日期']=pd.to_datetime(df1['截止日期'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])


df1 = pd.merge(df1, df, on=['证券代码', '截止日期'], how='left')
print(df1)
df1.loc[:,'截止日期']=df1['截止日期'].dt.year
print(df1)
df1.to_excel(os.path.join(path1,'加入成立年限.xlsx'),index=False)