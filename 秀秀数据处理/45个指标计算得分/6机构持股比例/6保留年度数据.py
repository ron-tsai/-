import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\6机构持股比例合并.xlsx',dtype=object,index_col=False)
df['截止月份']=pd.to_datetime(df['截止日期']).dt.month
# df.drop('Unnamed: 0')

df=df.loc[df['截止月份']==12]
# print(df)
df.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\6年度机构持股比例.xlsx')