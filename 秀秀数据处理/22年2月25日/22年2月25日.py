import pandas as pd
import os
path='/Users/ccmac/Desktop'
df=pd.read_excel(os.path.join(path,'FS_Comins.xlsx'),usecols=[0,1,2,3],header=None,skiprows=3,dtype=object,names=['证券代码','截止日期','报表类型','总资产周转率A'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])
df1=df.loc[(df['报表类型']=='A')&((df['截止日期']==pd.to_datetime('2007-12-31'))|(df['截止日期']==pd.to_datetime('2008-12-31'))|(df['截止日期']==pd.to_datetime('2009-12-31'))|(df['截止日期']==pd.to_datetime('2010-12-31'))|(df['截止日期']==pd.to_datetime('2011-12-31'))|(df['截止日期']==pd.to_datetime('2012-12-31'))|(df['截止日期']==pd.to_datetime('2013-12-31'))|
(df['截止日期']==pd.to_datetime('2014-12-31'))|
(df['截止日期']==pd.to_datetime('2015-12-31'))|
(df['截止日期']==pd.to_datetime('2016-12-31'))|
(df['截止日期']==pd.to_datetime('2017-12-31'))|
(df['截止日期']==pd.to_datetime('2018-12-31'))|
(df['截止日期']==pd.to_datetime('2019-12-31'))|
(df['截止日期']==pd.to_datetime('2020-12-31'))),:]


def get_cuo_wei_xiang_chu(df):

    if df['fenmu'] == 0:
        return 0
    else:
        return df['总资产周转率A'] / df['fenmu']


df0 = pd.DataFrame(columns=df1.columns)

g = df1.groupby('证券代码')

for name, group in g:


    group.set_index('截止日期', inplace=True, drop=True)


    print('group', group)







    group['fenmu']= group['总资产周转率A'].shift(1)



    group["GMP"] =group.apply(get_cuo_wei_xiang_chu, axis=1)
    print(group)
    df0 = df0.append(group)

print(df0)
# df0=df0.loc[:,~df0.columns.str.contains('Unnamed')]

df0.to_excel(os.path.join(path,'jieguo.xlsx'))