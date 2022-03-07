import pandas as pd
import os

path='/Users/ccmac/Desktop/情感分析存储'

year_list=[2017,2018,2019,2020,2021]
df0 = pd.read_excel(os.path.join(path, '2016年情感得分.xlsx'), dtype=object)
df0.loc[:, 'date'] = pd.to_datetime(df0['date']).dt.date
for year in year_list:

    file='/Users/ccmac/Desktop/情感分析存储/{}年情感得分.xlsx'.format(year)

    df = pd.read_excel(os.path.join(path, file), dtype=object)
    df.loc[:, 'date'] = pd.to_datetime(df['date']).dt.date

    df0 = pd.concat([df,df0])

    print(df0)





df0.to_excel(os.path.join(path,'年情感分析总表.xlsx'),index=False)
