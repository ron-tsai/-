import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'
df=pd.read_excel(os.path.join(path,'盈利得分和讯网.xlsx'),dtype=object,index=False,usecols=['证券代码','截止日期','和讯网盈利得分'])
print(df)
df.to_excel(os.path.join(path,'和讯网盈利得分-.xlsx'),index=False)