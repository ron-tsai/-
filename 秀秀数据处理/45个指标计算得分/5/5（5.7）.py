import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\5高管是否持股打分预处理(5.7).xlsx',dtype=object)
df=df.loc[:,~df.columns.str.contains('Unnamed')]
def get_gaoguanchigu(x):
    if x['持股数']>0:
        return 100
    if x['持股数']==0:
        return 0


df.loc[:,'评分']=df.apply(get_gaoguanchigu,axis=1)
print(df)

df.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\5高管是否持股打分(5.7).xlsx')
