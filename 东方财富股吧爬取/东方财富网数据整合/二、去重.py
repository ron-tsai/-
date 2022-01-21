
import pandas as pd
import os

path='/Users/ccmac/Desktop/2021'

df=pd.read_excel(os.path.join(path,'2021合并尝试.xlsx'),usecols=[1,2])



print(df[df.duplicated()] )
# df.drop_duplicates(subset=None,keep="first",inplace=True)

