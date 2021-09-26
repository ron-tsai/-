import pandas as pd
import os



path='F:\\newstart\software\category\\tool\category\deal_with_data\\1\合并数据'
df1=pd.read_csv(os.path.join(path,'1.csv'),usecols=['news_id','pub_date','overall_senti_score_adjust'],parse_dates=True)
df2=pd.read_csv(os.path.join(path,'2.csv'),usecols=['news_id','pub_date','overall_senti_score_adjust'],parse_dates=True)
df3=pd.concat([df1,df2],ignore_index=True,join='inner')
g=df3.groupby('pub_date')['overall_senti_score_adjust'].mean()
g_df=pd.DataFrame(g).reset_index()
g_df.to_excel(os.path.join(path,'6.xlsx'),index=False)
