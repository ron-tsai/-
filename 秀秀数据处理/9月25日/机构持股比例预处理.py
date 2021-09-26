import pandas as pd
import os
path1='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5\9.25'
df=pd.read_excel(os.path.join(path1,'机构持股比例.xlsx'),index=False,dtype=object)
df.loc[:,'year']=pd.to_datetime(df['year'])
df1=df.loc[((df['year']==pd.to_datetime('2010-12-31'))|(df['year']==pd.to_datetime('2011-12-31'))|(df['year']==pd.to_datetime('2012-12-31'))|(df['year']==pd.to_datetime('2013-12-31'))|
(df['year']==pd.to_datetime('2014-12-31'))|
(df['year']==pd.to_datetime('2015-12-31'))|
(df['year']==pd.to_datetime('2016-12-31'))|
(df['year']==pd.to_datetime('2017-12-31'))|
(df['year']==pd.to_datetime('2018-12-31'))|
(df['year']==pd.to_datetime('2019-12-31'))|
(df['year']==pd.to_datetime('2020-12-31'))),:]
df1.to_excel(os.path.join(path,'--机构持股比例.xlsx'),index=False)