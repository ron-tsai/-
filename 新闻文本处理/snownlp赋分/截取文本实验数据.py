import pandas as pd
import os
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df=pd.read_excel(os.path.join(path,'2012年.xlsx'),index_col='date',parse_dates=True)

df=df.loc[df.index<pd.to_datetime('2012-01-10'),:]

print(df)
save_path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df.to_excel(os.path.join(save_path,'文本情感分析实验数据.xlsx'))