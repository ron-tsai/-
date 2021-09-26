import pandas as pd
import os
import jqdatasdk as jd
jd.auth('18359196774','acginor1992CR')
date_init='2013-01-01'
stocks=jd.get_index_stocks('000300.XSHG',date=date_init)
print(len(stocks))
path='F:\\newstart\software\category\\tool\category\deal_with_data\股吧\股吧数据\看涨看跌中性\处理数据'
df=pd.read_excel(os.path.join(path,'2013.xlsx'),skiprows=2,names=['date','code','source','positive','neutral','negtive'],parse_dates=True,dtype=object)
g=df.groupby('date')['neutral'].sum()
print(g)