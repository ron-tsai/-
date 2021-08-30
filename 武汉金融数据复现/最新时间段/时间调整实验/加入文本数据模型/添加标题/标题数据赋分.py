import pandas as pd
import os
from snownlp import SnowNLP
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\标题赋分'

path2='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'

# file_list=os.listdir(path)



df1=pd.read_excel(os.path.join(path,'total_title.xlsx'),dtype=object,index=False)



title_score_list=[]
for title in df1['title']:
    score = SnowNLP(title)
    s = score.sentiments
    p=s-0.5
    title_score_list.append(p)
df1['title_score']=title_score_list
df1.to_excel(os.path.join(path,'title_score.xlsx'),index=False)