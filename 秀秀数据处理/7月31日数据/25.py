import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据'
df=pd.read_excel(os.path.join(path,'25 .xlsx'),usecols=[0,1,2],header=None,skiprows=3,dtype=object,names=['证券代码','截止日期','上市公司是否违规'])
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期'])

def get_score(x):
    if x['上市公司是否违规']=='N':
        return 100
    if x['上市公司是否违规']=='Y':
        return 0
df.loc[:,'分数']=df.apply(get_score,axis=1)




df.to_excel(os.path.join(path,'25-.xlsx'),index=False)