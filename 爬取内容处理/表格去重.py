import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\爬取内容\合并.xlsx')
df=df.drop_duplicates(keep='first')
df.to_excel('C:\\Users\Administrator\Desktop\爬取内容\去重.xlsx')