import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\我整理好的'
df_list=os.listdir(path)
for file in df_list:
    df=pd.read_excel(os.path.join(path,file),dtype=object,index=False)
    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df.drop_duplicates(subset=['证券代码','截止日期'],keep='first',inplace=True)


