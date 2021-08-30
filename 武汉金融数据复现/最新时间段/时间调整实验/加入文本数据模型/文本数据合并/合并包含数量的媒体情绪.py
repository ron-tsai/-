import pandas as pd
import os

path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\媒体情绪加总'

path2='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'

file_list=os.listdir(path)
df0=pd.DataFrame(columns=['date','sector_score'])
for file in file_list:

    df=pd.read_excel(os.path.join(path,file),dtype=object)

    df0=df0.append(df,ignore_index=False)
    print(df0)

print(df0)


df1=df0.loc[(df0['date']>=pd.to_datetime('2013-01-09'))&(df0['date']<=pd.to_datetime('2021-07-02')),:]
# df1.rename(columns={'date':'date','title':'media_attention'},inplace=True)
df2=pd.read_excel(os.path.join(path2,'guanzhudu_data.xlsx'))
df3=pd.merge(df1,df2,on='date',how='inner')
df3.to_excel(os.path.join(path2,'sum_data.xlsx'),index=False)