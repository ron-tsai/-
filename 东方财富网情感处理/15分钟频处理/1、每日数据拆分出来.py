import pandas as pd
import os
import datetime
import math
path='/Users/ccmac/Desktop/情感分析存储'

year=2021

file='/Users/ccmac/Desktop/情感分析存储/{}年情感分类合并.xlsx'.format(year)

df = pd.read_excel(os.path.join(path, file), dtype=object)
df['date_Day'] = pd.to_datetime(df['date']).dt.date
print(df)
# df0 = pd.DataFrame(columns=df.columns)



df_list=df['date_Day'].to_list()
new_list = list(set(df_list))
print(new_list)


score_list=[]
for idx in new_list:
    df0=df.loc[(df['date_Day']==pd.to_datetime(idx))]
    print(df0)
    path1 = '/Users/ccmac/Desktop/情感分析存储/{}年按日拆分'.format(year)

    df0.to_excel(os.path.join(path1,'{}.xlsx'.format(idx)),index=False)
