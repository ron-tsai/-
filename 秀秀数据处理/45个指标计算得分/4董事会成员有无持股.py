import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\4 .xlsx',skiprows=2,names=['证券代码','统计截止日期','董事会持股数量'],dtype=object)

print(df)
def get_dongshihuichengychigu(x):
    if x['董事会持股数量']>0:
        return 100
    if x['董事会持股数量']==0:
        return 0

df.loc[:,'评分']=df.apply(get_dongshihuichengychigu,axis=1)
print(df)
df.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\4董事会成员有无持股打分.xlsx')