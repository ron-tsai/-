import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\5  高管是否持股.xlsx',skiprows=2,names=['证券代码','日期','持股数'],dtype=object)
print(df)

def get_gaoguanchigu(x):
    if x['持股数']>0:
        return 100
    if x['持股数']==0:
        return 0

df.loc[:,'评分']=df.apply(get_gaoguanchigu,axis=1)

df.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\5高管是否持股打分.xlsx')