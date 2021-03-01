import pandas as pd
df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\利润表2处理完成.xlsx',header=0,converters = {'Stkcd':str})

df1=df1.query('Accper=="2011-12-31"& B001100000<10000000')
df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\营业收入小于一千万2.xlsx')
