import pandas as pd
import os
import requests
import re



path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\社会责任\社会责任爬取'
save_path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\社会责任爬取fillna'

df_list=os.listdir(path)
for file in df_list:
    df=pd.read_excel(os.path.join(path,file),dtype=object)
    print(df)
    df['截止日期'].replace({'NAN': None}, inplace=True, regex=True)
    df.loc[:,'截止日期']=df['截止日期'].fillna(method='ffill')
    df.loc[:,'截止日期']=df['截止日期'].fillna(method='bfill')
    df.loc[:,'截止日期']=df['截止日期'].fillna(method='ffill')
    df.loc[:,'截止日期']=df['截止日期'].fillna(method='bfill')
    df.loc[:,'截止日期']=df['截止日期'].fillna(method='ffill')
    df.loc[:,'截止日期']=df['截止日期'].fillna(method='bfill')
    df.loc[:, '截止日期']=df['截止日期'].str.replace('[年]','1231')
    print(df)
    df.loc[:,'截止日期']=pd.to_datetime(df['截止日期']).dt.date
    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    print(df)
    df.to_excel(os.path.join(save_path,file),index=False)



