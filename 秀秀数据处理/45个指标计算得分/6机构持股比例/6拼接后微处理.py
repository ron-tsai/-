import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\6机构持股比例合并.xlsx',dtype=object)
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期']).dt.date
df.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\6机构持股比例1.xlsx')
