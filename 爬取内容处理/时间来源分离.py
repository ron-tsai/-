import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\爬取内容\去重.xlsx')
date=df['date_source'].str[:11]
source=df['date_source'].str[21:]
df['date']=date
df['source']=source

df.drop('date_source',axis=1,inplace=True)
print(df.isnull())

df.to_excel('C:\\Users\Administrator\Desktop\爬取内容\时间来源分离.xlsx')