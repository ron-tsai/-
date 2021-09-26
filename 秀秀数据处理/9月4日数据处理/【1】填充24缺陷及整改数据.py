import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.4'
df=pd.read_excel(os.path.join(path,'【1】9月4日数据起始.xlsx'),dtype=object,index=False)
df['24内部控制缺陷及整改情况评分'].fillna(100,inplace=True)
# print(df['24内部控制缺陷及整改情况评分'])
df.sort_values(by=['ID','截止日期'],inplace=True)
df.to_excel(os.path.join(path,'【2】9月4日数据起始(填补了24数据).xlsx'),index=False)