import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'
df=pd.read_excel(os.path.join(path,'财务杠杆.xlsx'),usecols=[0,1,2,3],header=None,skiprows=3,dtype=object,names=['证券代码','截止日期','报表类型','资产负债率'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])
df1=df.loc[(df['报表类型']=='A')&((df['截止日期']==pd.to_datetime('2010-12-31'))|(df['截止日期']==pd.to_datetime('2011-12-31'))|(df['截止日期']==pd.to_datetime('2012-12-31'))|(df['截止日期']==pd.to_datetime('2013-12-31'))|
(df['截止日期']==pd.to_datetime('2014-12-31'))|
(df['截止日期']==pd.to_datetime('2015-12-31'))|
(df['截止日期']==pd.to_datetime('2016-12-31'))|
(df['截止日期']==pd.to_datetime('2017-12-31'))|
(df['截止日期']==pd.to_datetime('2018-12-31'))|
(df['截止日期']==pd.to_datetime('2019-12-31'))|
(df['截止日期']==pd.to_datetime('2020-12-31'))),:]
df1.to_excel(os.path.join(path,'caiwuganggan.xlsx'),index=False)