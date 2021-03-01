import pandas as pd
df1=pd.read_excel('C:\\Users\Administrator\Desktop\爬取内容\\得分表.xlsx')
df2=pd.read_excel('C:\\Users\Administrator\Desktop\爬取内容\\2020年爬取新闻.xlsx')
df=pd.concat([df1,df2],axis=1)
df.to_excel('C:\\Users\Administrator\Desktop\爬取内容\\合并表.xlsx')