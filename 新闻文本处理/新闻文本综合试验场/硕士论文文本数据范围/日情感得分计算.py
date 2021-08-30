import pandas as pd
import os
import numpy as np
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分'
df=pd.read_excel(os.path.join(path,'2013年赋分.xlsx'),)

ser=df.replace(0, np.nan).groupby(['date'])['sector_score'].sum()
ser=pd.DataFrame(ser)
ser.loc[:,'sector_score']=ser['sector_score'].fillna(0)
save_path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'

ser.to_excel(os.path.join(save_path,'sum2013.xlsx'))