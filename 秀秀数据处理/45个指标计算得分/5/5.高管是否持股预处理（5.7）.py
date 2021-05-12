import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\5（5.7）.xlsx',skiprows=2,names=['证券代码','日期','持股人','持股数'],dtype=object)
df.fillna({'持股数':0},inplace=True)
# print(df)

g=df.groupby(['证券代码','日期'])['持股数'].sum()
g_df=pd.DataFrame(g,columns=['持股数']).reset_index()
# g_df=pd.DataFrame(dict(list(g)))
g_df.loc[:,'证券代码']=g_df['证券代码'].fillna(method="ffill")
print(g_df)
# g_df.loc[:'证券代码']=g_df['证券代码'].fillna(method="ffill")
def get_gaoguanchigu(x):
    if x['持股数']>0:
        return 100
    if x['持股数']==0:
        return 0


g_df.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\5高管是否持股打分预处理(5.7).xlsx')
# g_df.loc[:,'评分']=df.apply(get_gaoguanchigu,axis=1)
# print(g_df)