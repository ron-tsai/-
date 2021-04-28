import pandas as pd
df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\\2017预处理数据.xlsx')
print(df['source'].value_counts())