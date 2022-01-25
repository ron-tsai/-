import pandas as pd


import os

path='/Users/ccmac/Desktop'

df=pd.read_excel(os.path.join(path,"2002.xlsx"),usecols=[1,2])

for time in df['time']:
    # df['time']=pd.to_datetime(df['time'])
    df['date']=pd.to_datetime(df['time'].add(' 2017'))


print(df)



# >>> pd.to_datetime(df['Date'].add(' 2021'), format="%B %d %Y")
#
# 0   2021-06-22
# 1   2021-06-23
# 2   2021-06-24
# 3   2021-06-25
# Name: Date, dtype: datetime64[ns]