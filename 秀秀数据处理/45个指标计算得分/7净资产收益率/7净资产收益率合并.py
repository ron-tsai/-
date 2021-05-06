import pandas as pd
df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\7\\7_1.xls',dtype=object,names=['证券代码','截止日期','净资产收益率'])
df2=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\7\\7_1.xls',dtype=object,names=['证券代码','截止日期','净资产收益率'])


df3=pd.concat([df1,df2],ignore_index=True,join='inner')
df3.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\7净资产收益率合并.xlsx')