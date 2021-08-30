import pandas as pd
import os
from snownlp import SnowNLP
path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\标题赋分'
df1=pd.read_excel(os.path.join(path,'合并标题和文本分数.xlsx'),dtype=object,index=False,usecols=['date','title_score','sector_score'])

df2=df1.fillna(method='ffill',axis=1)
df2.loc[:,'score']=df2['title_score']*0.3+df2['sector_score']*0.7
df2.to_excel(os.path.join(path,'添加标题计算完成.xlsx'),index=False)
