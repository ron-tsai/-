import pandas as pd
import os
path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安'
df=pd.read_excel(os.path.join(path,'2012.xlsx'),skiprows=2,usecols=[1,2,3,4],names=['date','title','content','source'],index_col='date',parse_dates=True)

df=df.loc[(df['source']=='上海证券报')|(df['source']=='中国证券报')|(df['source']=='证券时报')|(df['source']=='证券时报网')|(df['source']=='金融时报')|(df['source']=='经济日报')|(df['source']=='中国日报')|(df['source']=='证券市场周刊'),:]

save_path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df.to_excel(os.path.join(save_path,'2012年.xlsx'))
