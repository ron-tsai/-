import pandas as pd
import os
path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据'

df1=pd.read_excel(os.path.join(path_dir,'沪深300日频数据（16年起始）.xlsx'),skiprows=3,names=['指数代码','trade_time','open','high','low','close','volume'],dtype=object)
df2=pd.read_excel(os.path.join(path_dir,'沪深300日频数据（16年止）.xlsx'),skiprows=3,names=['指数代码','trade_time','open','high','low','close','volume'],dtype=object)
df3=pd.concat([df1,df2],ignore_index=True,join='inner')
df3.drop_duplicates(inplace=True)

print(df3)
df3.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\step1：日频原数据拼接去重.xlsx')