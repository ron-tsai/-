import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\爬取内容\表格空白上移.xlsx')
df.dropna(how='all',inplace=True)
df.reset_index(drop=True, inplace=True)

df.to_excel('C:\\Users\Administrator\Desktop\爬取内容\打磨1.xlsx')
