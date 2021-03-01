import pandas as pd
import numpy as np
df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\利润表删减.xlsx',header=0,converters = {'Symbol':str})
g=df1.groupby('Symbol')
for name,group in g:
    if group['NetProfit'].values.all() <0:
        print(name)
