import pandas as pd
df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\利润表删减.xlsx',header=0,converters = {'Symbol':str})
# df2=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\审计表删减.xlsx',header=0,converters = {'Symbol':str})


# 净资产
# df1=df1.query('EndDate=="2011-12-31" & NAVPS<0')
# df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\违反净资产.xlsx')
# 净利润
df1=df1.query('NetProfit<0')
df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\净利润连续两年小于0.xlsx')
