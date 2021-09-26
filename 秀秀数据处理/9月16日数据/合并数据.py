import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5\9.16合并'

path1='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'


df_list=os.listdir(path)
df1=pd.read_excel(os.path.join(path1,'didd数据.xlsx'),dtype=object)
# df1.loc[:,'Year']=pd.to_datetime(df1['Year'])
print(df1)

for file in df_list:
    df=pd.read_excel(os.path.join(path,file),dtype=object,index=False)
    df.loc[:, 'Year'] = pd.to_datetime(df['Year'])
    df.loc[:, 'Year'] = df['Year'].dt.year
    print('df',df)
    # df['Year'].astype('int64')



    # print(df)

    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df1 = pd.merge(df1, df, on=['Stkcd', 'Year'], how='left')
    print('df1',df1)

df1.to_excel(os.path.join(path, '合并尝试.xlsx'))