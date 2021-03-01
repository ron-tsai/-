import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\爬取内容\表格空白上移.xlsx')

df.loc[:,'date']=df['date'].str.replace('[年月日]','')
df.loc[:,'source']=df['source'].str.replace('：','')

df.set_index(pd.to_datetime(df['date']).dt.date,inplace=True)
df.drop('date',axis=1,inplace=True)
df.sort_index(inplace=True)

df.to_excel('C:\\Users\Administrator\Desktop\爬取内容\时间处理.xlsx')