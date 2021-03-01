import pandas as pd
import numpy as np
df=pd.read_excel('C:\\Users\Administrator\Desktop\爬取内容\\情感得分合并表.xlsx')
df.set_index(pd.to_datetime(df['date'].dt.date),inplace=True)
df.drop('date',axis=1,inplace=True)
g=df.groupby('date')['情感得分'].agg(np.mean)
df_date=pd.DataFrame(g)

pdates=pd.date_range(start='2020-01-01',end='2020-12-31')
df_date_new=g.reindex(pdates,fill_value=0.5)

df_date_new.to_excel('C:\\Users\Administrator\Desktop\爬取内容\\情感得分平均.xlsx')