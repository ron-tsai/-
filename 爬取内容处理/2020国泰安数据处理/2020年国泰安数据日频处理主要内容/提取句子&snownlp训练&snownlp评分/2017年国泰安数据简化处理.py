import pandas as pd

df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\\2017year.xlsx',skiprows=3,header=None,names=['ID','date','title','date2','content','source'])
df.drop(['date','ID','date2'],axis=1,inplace=True)
save_path ='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\\2017预处理数据.xlsx'
df.to_excel(save_path)
