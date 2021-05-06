import pandas as pd

df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\27 28 29 30 .xlsx',dtype=object,skiprows=2,names=['证券代码','证券简称','会计截止日期','实际披露日'])
# print(df)
# df.loc[:,'会计截止日期']=pd.to_datetime(df['会计截止日期'])
df['截止月份']=pd.to_datetime(df['会计截止日期']).dt.month
df1=df.loc[df['截止月份']==3,:]
df2=df.loc[df['截止月份']==6,:]
df3=df.loc[df['截止月份']==9,:]
df4=df.loc[df['截止月份']==12,:]
# print(df1)


def get_gongbujishixing(x):

    a=pd.to_datetime(x['实际披露日']).month


    if (x['截止月份']==3) & (a <= 4):
        return 100
    if (x['截止月份']==3) & (a> 4):
        return 0
    if (x['截止月份']==6) & (a <= 8):
        return 100
    if (x['截止月份']==6) & (a> 8):
        return 0
    if (x['截止月份']==9) & (a <= 10):
        return 100
    if (x['截止月份']==9) & (a > 10):
        return 0
    if (x['截止月份']==12) & (a <= 4):
        return 100
    if (x['截止月份']==12) & (a > 4):
        return 0

# for df in[df1,df2,df3,df4]:
#     df.loc[:, '评分'] = df.apply(get_gongbujishixing, axis=1)
#     df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\一季度报告及时性打分.xlsx')

df1.loc[:,'评分']=df1.apply(get_gongbujishixing,axis=1)
df2.loc[:,'评分']=df2.apply(get_gongbujishixing,axis=1)
df3.loc[:,'评分']=df3.apply(get_gongbujishixing,axis=1)
df4.loc[:,'评分']=df4.apply(get_gongbujishixing,axis=1)
# df1.set_index(['证券代码','会计截止日期','报告类型'],inplace=True)

print(df1)
df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\一季度报告及时性打分.xlsx')
df2.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\二季度报告及时性打分.xlsx')
df3.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\三季度报告及时性打分.xlsx')
df4.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\年报告及时性打分.xlsx')