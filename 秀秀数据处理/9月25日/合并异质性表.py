import pandas as pd
import os
import numpy as np
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5\9.25'

path1='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'


df_list=os.listdir(path)
df1=pd.read_excel(os.path.join(path1,'----异质性分析.xlsx'),dtype=object,index=False)
# df1.loc[:,'Year']=pd.to_datetime(df1['Year'])
print(df1)

for file in df_list:
    df=pd.read_excel(os.path.join(path,file),dtype=object,index=False)
    df.loc[:, 'year'] = pd.to_datetime(df['year'])
    df.loc[:, 'year'] = df['year'].dt.year
    print('df',df)
    # df['Year'].astype('int64')



    # print(df)

    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df1 = pd.merge(df1, df, on=['Stkcd', 'year'], how='left')
    print('df1',df1)

def get_guquan(x):

    if x['股权性质']!='国企':
        return 0
    if x['股权性质']=='国企':
        return 1
df1.loc[:,'SOE']=df1.apply(get_guquan,axis=1)


# jigouchigubi=np.mean(df1['机构持股比例'])
# def get_jigou(x):
#
#     if x['机构持股比例']>=jigouchigubi:
#         return 1
#     if x['机构持股比例']<jigouchigubi:
#         return 0
# df1.loc[:,'Inv']=df1.apply(get_jigou,axis=1)

df1.to_excel(os.path.join(path, '异质性合并.xlsx'),index=False)