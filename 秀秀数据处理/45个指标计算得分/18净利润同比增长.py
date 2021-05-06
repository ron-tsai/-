import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\18 归属母公司股东的净利润同比增长率.xlsx',names=['证券代码','截止日期','报表类型','归属于母公司净利润增长率'],skiprows=2,dtype=object,index_col=False)
print(df)
df['截止月份']=pd.to_datetime(df['截止日期']).dt.month
# df.drop('Unnamed: 0')

df=df.loc[(df['截止月份']==12)&(df['报表类型']=='A')]
print(df)
df.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\18归属母公司股东的净利润同比增长率.xlsx')