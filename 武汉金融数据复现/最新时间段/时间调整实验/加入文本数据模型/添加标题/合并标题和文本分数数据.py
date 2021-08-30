import pandas as pd
import os
from snownlp import SnowNLP
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\标题赋分'

path2='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\文本内容合并'
df1=pd.read_excel(os.path.join(path,'title_score.xlsx'),dtype=object,index=False)
df2=pd.read_excel(os.path.join(path2,'内容得分合并.xlsx'),dtype=object,index=False)
df3=pd.merge(df1,df2,on=['date','title'],how='inner')
df3.to_excel(os.path.join(path,'合并标题和文本分数.xlsx'),index=False)
