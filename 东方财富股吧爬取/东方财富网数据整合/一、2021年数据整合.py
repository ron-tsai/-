import pandas as pd
import os

path='/Users/ccmac/Desktop/2021'


path1='/Users/ccmac/Desktop'




df_list=os.listdir(path)
df1=pd.DataFrame(columns=['time','title'])
for file in df_list:
    df=pd.read_excel(os.path.join(path,file),dtype=object,usecols=['time','title'])
    print(df)

    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df1 = pd.merge(df1, df, on=['time', 'title'], how='outer')
    print(df1)
df1.to_excel(os.path.join(path1, '2021合并尝试.xlsx'))