import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5'
# path1='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.5\控制变量合并'
df=pd.read_excel(os.path.join(path,'DID数据916.xlsx'),dtype=object,index=False)
# df1=pd.read_excel(os.path.join(path1,'添加时间控制变量.xlsx'),dtype=object)
df.loc[(df['Year']==2012),'Time']=1
# print(df.loc[(df['Year']==2012),'Time'])
df.to_excel(os.path.join(path,'DID数据（2012修改）.xlsx'))