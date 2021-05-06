import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\16（5.5‘）.xlsx',skiprows=2,dtype=object,index_col=False,names=['证券代码','截止日期','报表类型','资产负债率'])
df['截止月份']=pd.to_datetime(df['截止日期']).dt.month
# df.drop('Unnamed: 0')

df=df.loc[(df['截止月份']==12)&(df['报表类型']=='A')]
print(df)
df.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\16营业收入同比增长率(5.5).xlsx.xlsx')