import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\我整理好的'
# save_path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据'
df1=pd.read_excel(os.path.join(path,'27  一季度报告及时性打分.xlsx'),dtype=object)
df2=pd.read_excel(os.path.join(path,'28  二季度报告及时性打分.xlsx'),dtype=object)
df3=pd.read_excel(os.path.join(path,'29  三季度报告及时性打分.xlsx'),dtype=object)
df1.loc[:,'截止日期']=pd.to_datetime(df1['截止日期'])
df2.loc[:,'截止日期']=pd.to_datetime(df1['截止日期'])
df3.loc[:,'截止日期']=pd.to_datetime(df1['截止日期'])
def get_date(x):
    if (x['截止日期']>=pd.to_datetime('2010-01-01'))&(x['截止日期']<=pd.to_datetime('2010-12-31')):
        return pd.to_datetime('2010-12-31')
    if (x['截止日期']>=pd.to_datetime('2011-01-01'))&(x['截止日期']<=pd.to_datetime('2011-12-31')):
        return pd.to_datetime('2011-12-31')
    if (x['截止日期']>=pd.to_datetime('2012-01-01'))&(x['截止日期']<=pd.to_datetime('2012-12-31')):
        return pd.to_datetime('2012-12-31')
    if (x['截止日期']>=pd.to_datetime('2013-01-01'))&(x['截止日期']<=pd.to_datetime('2013-12-31')):
        return pd.to_datetime('2013-12-31')
    if (x['截止日期']>=pd.to_datetime('2014-01-01'))&(x['截止日期']<=pd.to_datetime('2014-12-31')):
        return pd.to_datetime('2014-12-31')
    if (x['截止日期']>=pd.to_datetime('2015-01-01'))&(x['截止日期']<=pd.to_datetime('2015-12-31')):
        return pd.to_datetime('2015-12-31')
    if (x['截止日期']>=pd.to_datetime('2016-01-01'))&(x['截止日期']<=pd.to_datetime('2016-12-31')):
        return pd.to_datetime('2016-12-31')
    if (x['截止日期']>=pd.to_datetime('2017-01-01'))&(x['截止日期']<=pd.to_datetime('2017-12-31')):
        return pd.to_datetime('2017-12-31')
    if (x['截止日期']>=pd.to_datetime('2018-01-01'))&(x['截止日期']<=pd.to_datetime('2018-12-31')):
        return pd.to_datetime('2018-12-31')
    if (x['截止日期']>=pd.to_datetime('2019-01-01'))&(x['截止日期']<=pd.to_datetime('2019-12-31')):
        return pd.to_datetime('2019-12-31')
    if (x['截止日期']>=pd.to_datetime('2020-01-01'))&(x['截止日期']<=pd.to_datetime('2020-12-31')):
        return pd.to_datetime('2020-12-31')
df1.loc[:,'截止日期1']=df1.apply(get_date,axis=1)
df2.loc[:,'截止日期1']=df2.apply(get_date,axis=1)
df3.loc[:,'截止日期1']=df3.apply(get_date,axis=1)

df1.to_excel(os.path.join(path,'27.xlsx'))
df2.to_excel(os.path.join(path,'28.xlsx'))
df3.to_excel(os.path.join(path,'29.xlsx'))