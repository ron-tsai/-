import pandas as pd
from datetime import datetime as dt
import numpy as np
df=pd.read_excel('C:\\Users\Administrator\Desktop\\27 28 29 30.xlsx',skiprows=3,names=['证券代码','证券简称','报告类型','会计截止日期','报告公布日期'],dtype=object)



df['报告公布日期']=pd.to_datetime(df['报告公布日期'])




def get_gongbujishixing(x):

    a=pd.to_datetime(x['报告公布日期']).month
    print(a)
    print(x['报告类型'])

    if (x['报告类型'] == 1) & (a <= 4):
        return 100
    if (x['报告类型'] == 1) & (a> 4):
        return 0
    if (x['报告类型'] == 2) & (a <= 8):
        return 100
    if (x['报告类型'] == 2) & (a> 8):
        return 0
    if (x['报告类型'] == 3) & (a <= 10):
        return 100
    if (x['报告类型'] == 3) & (a > 10):
        return 0
    if (x['报告类型'] == 4) & (a <= 4):
        return 100
    if (x['报告类型'] == 4) & (a > 4):
        return 0
df.loc[:,'评分']=df.apply(get_gongbujishixing,axis=1)
print(df)
df.to_excel('C:\\Users\Administrator\Desktop\\报告及时性打分.xlsx')