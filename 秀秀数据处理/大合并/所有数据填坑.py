import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\我整理好的'
save_path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据'
date_index=pd.date_range('20101231','20201231',freq='Y')
df_list=os.listdir(path)
df1=pd.read_excel(os.path.join(path,'24-.xlsx'),dtype=object,usecols=['截止日期','证券代码'])
df1.loc[:,'截止日期']=pd.to_datetime(df1['截止日期']).dt.date
for file in df_list:
    df=pd.read_excel(os.path.join(path,file),dtype=object,index=False)
    df.loc[:,'截止日期']=pd.to_datetime(df['截止日期']).dt.date
    df.drop_duplicates(subset=['证券代码', '截止日期'], keep='first', inplace=True)
    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df0 = pd.DataFrame(columns=df.columns)

    print('df0',df0)
    g = df.groupby('证券代码')
    for name, group in g:

        group.set_index('截止日期',inplace=True,drop=True)




        group=group.reindex(date_index)
        group.loc[:, '证券代码'] = group['证券代码'].fillna(name)
        print('group', group)
        print('group的长度', len(group))
        # group.loc[:, '截止日期'] = group.index
        df0 = df0.append(group)
        print('小group合并',df0)
    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df1 = pd.merge(df1, df, on=['证券代码', '截止日期'], how='outer')
    df1.to_excel(os.path.join(save_path,'合并查看.xlsx'),index=False)