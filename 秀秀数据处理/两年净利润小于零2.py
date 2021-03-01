import pandas as pd
df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\利润表2处理完成.xlsx',header=0,converters = {'Stkcd':str})

df1=df1.query('(Accper=="2011-12-31" & B002000000<0) or (Accper=="2010-12-31" & B002000000<0)')
# df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\连续两年净利润小于零2.xlsx')
df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\净利润连续两年小于零2.xlsx')

