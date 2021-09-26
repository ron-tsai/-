import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.4'
df=pd.read_excel(os.path.join(path,'【4】9月4日数据pandas填充.xlsx'),dtype=object,index=False)


l=df['证券代码'].unique()
print(l)
def get_ID(x):
    for i,v in  enumerate(l):
        if x['证券代码'] ==v:
            return i+1

df.loc[:,'ID']=df.apply(get_ID,axis=1)
print(df['ID'])
df.to_excel(os.path.join(path, '【5】9月4日数据pandas修改ID.xlsx'), index=False)
