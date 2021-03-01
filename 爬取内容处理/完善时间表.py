import pandas as pd

df=pd.read_excel('C:\\Users\Administrator\Desktop\爬取内容\内容补充完成.xlsx')
df.set_index(df['date'].dt.date,inplace=True)
df.drop('date',axis=1,inplace=True)


df.sort_index(ascending=True,inplace=True)


df.to_excel('C:\\Users\Administrator\Desktop\爬取内容\完整时间处理2.0.xlsx')