import pandas as pd
df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\每股净资产2.xlsx',header=0,converters = {'Stkcd':str})
df1.drop([0,1],inplace=True)
df1=df1.query('Accper=="2011-12-31" & Typrep=="A" & F091001A<0')
df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\净资产小于零2.xlsx')


