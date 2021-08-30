import pandas as pd
import os
from snownlp import SnowNLP
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\标题赋分'

path2='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'

file_list=os.listdir(path)
df0=pd.DataFrame(columns=['date','title'])
for file in file_list:

    df=pd.read_excel(os.path.join(path,file),dtype=object,usecols=['date','title'])

    df0=df0.append(df,ignore_index=False)


df1=df0.loc[(df0['date']>=pd.to_datetime('2013-01-09'))&(df0['date']<=pd.to_datetime('2021-07-02')),:]
df1.to_excel(os.path.join(path,'total_title.xlsx'),index=False)
# title_score_list=[]
# for title in df1['title']:
#     score = SnowNLP(title)
#     print(score)
