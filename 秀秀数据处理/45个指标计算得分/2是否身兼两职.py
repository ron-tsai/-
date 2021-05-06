import pandas as pd

df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\2.xlsx',skiprows=2,dtype=object,names=['证券代码','统计截止日期','董事长与总经理兼任情况',1,2,3])
df=df.loc[:,['证券代码','统计截止日期','董事长与总经理兼任情况']]
print(df)

def get_shifoushenjianliangzhi(x):



    if x['董事长与总经理兼任情况']==2:
        return 100
    if  x['董事长与总经理兼任情况']==1:
        return 0

df.loc[:,'评分']=df.apply(get_shifoushenjianliangzhi,axis=1)
print(df)
df.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\2董事长与总经理兼任情况打分.xlsx')