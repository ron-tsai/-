import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据'
df=pd.read_excel(os.path.join(path,'24 .xlsx'),usecols=[0,1,2,3],header=None,skiprows=3,dtype=object,names=['证券代码','截止日期','缺陷类型','内控缺陷整改情况'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])

def get_score(x):
    if ((x['缺陷类型']=='重大缺陷')&(x['内控缺陷整改情况']=='未得到整改'))|((x['缺陷类型']=='重要缺陷')&(x['内控缺陷整改情况']=='未得到整改'))|((x['缺陷类型']=='重要缺陷')&(x['内控缺陷整改情况']==None))|((x['缺陷类型']=='重大缺陷')&(x['内控缺陷整改情况']==None)):
        return 0
    if ((x['缺陷类型']=='一般缺陷')&(x['内控缺陷整改情况']=='未得到整改'))|((x['缺陷类型']=='一般缺陷')&(x['内控缺陷整改情况']==None)):
        return 20
    if (x['缺陷类型']=='一般缺陷')&(x['内控缺陷整改情况']=='部分得到整改'):
        return 40
    if ((x['缺陷类型']=='重大缺陷')&(x['内控缺陷整改情况']=='部分得到整改'))|((x['缺陷类型']=='重要缺陷')&(x['内控缺陷整改情况']=='部分得到整改')):
        return 60
    if (x['内控缺陷整改情况']=='已得到整改'):
        return 80
df.loc[:,'分数']=df.apply(get_score,axis=1)


df.loc[:,'分数']=df['分数'].fillna(0)


date_index=pd.date_range('20101231','20201231',freq='Y')
print(date_index)

g=df.groupby('证券代码')

df0=pd.DataFrame({'截止日期':[],'证券代码':[],'缺陷类型':[],'内控缺陷整改情况':[],'分数':[]})

for name,group in g:

    group.sort_values(by=['截止日期','分数'],ascending=[True,True])

    group.drop_duplicates('截止日期','last',inplace=True)




    group.set_index('截止日期',inplace=True)

    group=group.reindex(date_index)

    group.loc[:,'证券代码']=group['证券代码'].fillna(name)
    group.loc[:,'分数']=group['分数'].fillna(100)
    group.loc[:,'截止日期']=group.index
    # group.set_index('证券代码',inplace=True)


    df0=df0.append(group)
    print(df0)
df0.to_excel(os.path.join(path,'24-.xlsx'),index=False)
