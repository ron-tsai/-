import pandas as pd

df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\\副本2020year.xlsx',skiprows=3,header=None,names=['ID','date','title','content','source'])

df.set_index(pd.to_datetime(df['date']),inplace=True) ###本来就无分秒无需'.dt.date'

df.drop(['date','ID'],axis=1,inplace=True)

df.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\\2020国泰安简化数据.xlsx')

###报错zipfile.LargeZipFile: Filesize would require ZIP64 extensions