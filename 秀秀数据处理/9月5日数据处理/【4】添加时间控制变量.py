import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'
path1='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5\控制变量合并'

df=pd.read_excel(os.path.join(path1,'合并且修改ID.xlsx'),dtype=object)

def get_time_kongzhi(x):
    if x['截止日期']<=pd.to_datetime('2013'):
        return 0
    if x['截止日期']>pd.to_datetime('2013'):
        return 1
df.loc[:,'t']=df.apply(get_time_kongzhi,axis=1)

df['break']=0
df.to_excel(os.path.join(path1,'添加时间控制变量.xlsx'),index=False)