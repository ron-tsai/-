import pandas as pd
# df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\利润表删减.xlsx',header=0,converters = {'Symbol':str})
df2=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\审计表删减.xlsx',header=0,converters = {'Symbol':str})


# 净资产
df2=df2.query('EndDate=="2011-12-31" & TypeAuditOpin=="无法发表意见"')

df2.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\违反审计意见退市规定.xlsx')
