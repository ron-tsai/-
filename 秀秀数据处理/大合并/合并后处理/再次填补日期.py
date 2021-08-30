import pandas as pd
import os


path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据'
date_index=pd.date_range('20101231','20201231',freq='Y')

df=pd.read_excel(os.path.join(path,'合并查看.xlsx'),dtype=object)
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期']).dt.date

g = df.groupby('证券代码')
df0 = pd.DataFrame(columns=df.columns)
for name, group in g:

    group.set_index('截止日期',inplace=True,drop=True)




    group=group.reindex(date_index)
    group.loc[:, '证券代码'] = group['证券代码'].fillna(name)
    group.loc[:, '截止日期'] = group.index
    print('group', group)
    print('group的长度', len(group))
    # group.loc[:, '截止日期'] = group.index
    df0 = df0.append(group)
    print('小group合并',df0)
df0=df0.loc[:,~df0.columns.str.contains('Unnamed')]
df0.to_excel(os.path.join(path,'填坑.xlsx'),index=False)