import pandas as pd
import os
path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据'

df1=pd.read_excel(os.path.join(path_dir,'沪深300日频数据（16年起始）.xlsx'),skiprows=2,names=['指数代码','trade_time','open','high','low','close','volume'],dtype=object)
print(df1)
df2=pd.read_excel(os.path.join(path_dir,'沪深300日频数据（16年止）.xlsx'),skiprows=2,names=['指数代码','trade_time','open','high','low','close','volume'],dtype=object)
print(df2)
df3=pd.concat([df1,df2],ignore_index=True,join='inner')
df3.drop_duplicates(inplace=True)

df3.sort_values(by='trade_time',inplace=True)
# print(df3)
df3.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\step1：日频原数据拼接去重.xlsx')