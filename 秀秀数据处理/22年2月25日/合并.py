import pandas as pd
import os

path='/Users/ccmac/Desktop'



df=pd.read_excel(os.path.join(path,'jieguo.xlsx'),dtype=object,usecols=['year','stkcd','GMP'])
df1=pd.read_excel(os.path.join(path,'全要素生产率3.xlsx'),dtype=object)

df1.loc[:,'year']=pd.to_datetime(df1['year'],format='%Y').dt.year
print(df1)
df.loc[:,'year']=pd.to_datetime(df['year']).dt.year
print(df)

df2 = pd.merge(df1, df, on=['year','stkcd'], how='outer')
print(df2)
df2.to_excel(os.path.join(path,'全要素生产率.xlsx'),index=False)