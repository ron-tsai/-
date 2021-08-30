import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\最终2010-2020'
df=pd.read_excel(os.path.join(path,'39 40-（日期修改为1231）.xlsx'),dtype=object)


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
df.loc[:,'截止日期1']=df.apply(get_date,axis=1)
df.to_excel(os.path.join(path,'39 40.xlsx'))