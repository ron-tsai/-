import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'
path1='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5\控制变量合并'



df_list=os.listdir(path1)
df1=pd.read_excel(os.path.join(path,'得分数据.xlsx'),dtype=object,usecols=['截止日期','证券代码'])
for file in df_list:
    df=pd.read_excel(os.path.join(path1,file),dtype=object)
    print(df)

    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df1 = pd.merge(df1, df, on=['证券代码', '截止日期'], how='left')
    print(df1)
df1.to_excel(os.path.join(path1,'合并尝试.xlsx'))