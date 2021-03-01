import pandas as pd
df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\利润表2.xlsx',header=0,converters = {'Symbol':str})
df1.drop([0,1],inplace=True)
df1=df1.query('(Accper=="2011-12-31"or Accper=="2010-12-31")& Typrep=="A"')

df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\利润表2处理完成.xlsx')
