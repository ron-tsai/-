import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据'
df=pd.read_excel(os.path.join(path,'22.xlsx'),usecols=[0,1,2],header=None,skiprows=3,dtype=object,names=['证券代码','截止日期','审计意见类型'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])

def get_score(x):
    if x['审计意见类型']=='标准无保留意见':
        return 100
    if x['审计意见类型']=='无保留意见加事项段':
        return 75
    if x['审计意见类型']=='保留意见':
        return 50
    if x['审计意见类型']=='无法表示意见':
        return 25
    if x['审计意见类型']=='否定意见':
        return 0
df.loc[:,'分数']=df.apply(get_score,axis=1)




df.to_excel(os.path.join(path,'22-.xlsx'),index=False)