import pandas as pd
import os
import numpy as np
path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\最初文本'
path2='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\媒体关注度聚合'

file_list=os.listdir(path)
df0=pd.DataFrame(columns=['date','title'])
for file in file_list:
    df = pd.read_excel(os.path.join(path,file), skiprows=2, usecols=[1, 2, 3, 4],
                       names=['date', 'title', 'content', 'source'], index_col='date', parse_dates=True)


    g=df.groupby('date')['title'].count()
    # g_df=pd.DataFrame(g,columns=['media_attention']).reset_index()
    g_df=pd.DataFrame(g).reset_index()

    print(g_df)
    df0=df0.append(g_df,ignore_index=False)
    print(df0)

print(df0)


df1=df0.loc[(df0['date']>=pd.to_datetime('2013-01-09'))&(df0['date']<=pd.to_datetime('2021-07-02')),:]
df1.rename(columns={'date':'date','title':'media_attention'},inplace=True)

df1.to_excel(os.path.join(path2,'media_attention.xlsx'),index=False)