import pandas as pd
import os

path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\标题赋分'
path2='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\标题赋分\用于合并数据'
df1=pd.read_excel(os.path.join(path,'添加标题计算完成.xlsx'),dtype=object,index=False,usecols=['date','sector_score'])
df1['sector_score']=df1['sector_score'].astype('float')
# print(df1.dtypes)
g=df1.groupby('date')['sector_score'].mean()
# print(g)
g_df=pd.DataFrame(g).reset_index()
df2=pd.read_excel(os.path.join(path2,'guanzhudu_data.xlsx'),dtype=object,index=False)
df3=pd.read_excel(os.path.join(path2,'media_attention.xlsx'),dtype=object,index=False)

df4=pd.merge(g_df,df2,on=['date'],how='inner')
df5=pd.merge(g_df,df3,on=['date'],how='inner')

df4.to_excel(os.path.join(path2,'finally2.xlsx'),index=False)
df5.to_excel(os.path.join(path2,'finally3.xlsx'),index=False)


