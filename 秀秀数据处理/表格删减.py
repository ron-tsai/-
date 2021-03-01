import pandas as pd
df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\利润表.xlsx',header=0,converters = {'Symbol':str})
df2=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\审计表.xlsx',header=0,converters = {'Symbol':str})
df1.drop([0,1],inplace=True)
df2.drop([0,1],inplace=True)
# df1[:,'EndDate']=df1['EndDate'].replace('-','')
# df2[:,'EndDate']=df2['EndDate'].replace('-','')
#
# df1.set_index(pd.to_datetime(df1['EndDate']).dt.date,inplace=True)
# df1.drop('EndDate',axis=1,inplace=True)
# df2.set_index(pd.to_datetime(df2['EndDate']).dt.date,inplace=True)
# df2.drop('EndDate',axis=1,inplace=True)
df1=df1.query('EndDate=="2011-12-31"or EndDate=="2010-12-31"')
df2=df2.query('EndDate=="2011-12-31"or EndDate=="2010-12-31"')


df1.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\利润表删减.xlsx')
df2.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\审计表删减.xlsx')


