import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\和讯网盈利得分'
save_path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\和讯网盈利得分'

df_list=os.listdir(path)
df1=pd.DataFrame({'证券代码':[],'截止日期':[],'和讯网盈利得分':[]})
for file in df_list:
    df=pd.read_excel(os.path.join(path,file),dtype=object)
    print(df)

    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df1=pd.merge(df1,df,on=['证券代码','截止日期','和讯网盈利得分'],how='outer')
    print(df1)

df1.sort_values(by=['证券代码','截止日期'],inplace=True)
df1=df1[['证券代码','截止日期','和讯网盈利得分']]
df1.to_excel(os.path.join(save_path,'和讯网盈利得分merge.xlsx'),index=False)