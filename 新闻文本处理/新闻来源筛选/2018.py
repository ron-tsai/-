import pandas as pd
import os

path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安'
df=pd.read_excel(os.path.join(path,'2018year.xlsx'),skiprows=2,usecols=[1,2,4,5],names=['date','title','content','source'],index_col='date',parse_dates=True)

df=df.loc[(df['source']=='上海证券报')|(df['source']=='证券时报')|(df['source']=='中国证券报')|(df['source']=='证券日报')|(df['source']=='第一财经报')|(df['source']=='21世纪经济报道'),:]

print(df)
save_path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成'
df.to_excel(os.path.join(save_path,'2018年.xlsx'))


