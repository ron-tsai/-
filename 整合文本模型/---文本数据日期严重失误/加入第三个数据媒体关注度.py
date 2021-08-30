import pandas as pd
import os

path='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\媒体关注度计算'
path2='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'
new_dir='F:\\newstart\software\category\\tool\category\deal_with_data\数据二合为一'

file_list=os.listdir(path)
df0=pd.DataFrame(columns=['date','title'])
for file in file_list:

    df=pd.read_excel(os.path.join(path,file),dtype=object)
    g=df.groupby('date')['title'].count()
    # g_df=pd.DataFrame(g,columns=['media_attention']).reset_index()
    g_df=pd.DataFrame(g).reset_index()

    print(g_df)
    df0=df0.append(g_df,ignore_index=False)
    print(df0)

print(df0)


# df1=df0.loc[(df0['date']>=pd.to_datetime('2013-01-09'))&(df0['date']<=pd.to_datetime('2021-07-02')),:]
df0.rename(columns={'date':'trade_time','title':'media_attention'},inplace=True)
df2=pd.read_excel(os.path.join(new_dir,'加了关注度再加媒体情绪.xlsx'),dtype=object)



df=pd.merge(df2,df0,on='trade_time',how='left')

df.to_excel(os.path.join(new_dir,'加了第三个媒体关注度.xlsx'),index=False)