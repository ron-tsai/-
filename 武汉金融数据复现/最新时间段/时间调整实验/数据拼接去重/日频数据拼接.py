import pandas as pd
import os
dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础\数据拼接'
df1=pd.read_excel(os.path.join(dir,'step1：日频原数据拼接去重.xlsx'),dtype=object,index=False)
df1=df1.loc[:,~df1.columns.str.contains('Unnamed')]
df2=pd.read_excel(os.path.join(dir,'沪深300日频数据（2021-2021-7-5）.xlsx'),dtype=object,skiprows=3,header=None,names=['指数代码','trade_time','open','high','low','close','volume'])
df=pd.concat([df1,df2],ignore_index=True,join='inner')
df.drop_duplicates(subset=None,keep='first',inplace=True)
df.loc[:,'trade_time']=pd.to_datetime(df['trade_time'])
df.sort_values(by='trade_time',ascending=False)
save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础'

df.to_excel(os.path.join(save_dir,'至7月日频数据.xlsx'))