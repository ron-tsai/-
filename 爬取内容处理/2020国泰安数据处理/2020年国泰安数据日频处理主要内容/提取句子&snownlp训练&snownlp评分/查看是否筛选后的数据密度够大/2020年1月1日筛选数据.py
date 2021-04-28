import pandas as pd
df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\按日拆分\\2020-01-01.xlsx')
df=df.query("source=='证券时报网'|source=='中国证券网'|source=='证券时报'|source=='中国证券报'|source=='东方财富网'|source=='证券日报'|source=='上海证券报'")
df.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\\2020年1月1日国泰安报纸筛选.xlsx')

