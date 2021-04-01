import pandas as pd
import numpy as np
for i in range(1,13):
    path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年{}月.xlsx'.format(i)
    df=pd.read_excel(path,index_col='date',parse_dates=True)
    df.index=df.index.date
    date_list = np.unique(df.index.values.tolist()).tolist()

    for datetime in date_list:
        df1=df.loc[df.index==datetime,:]
        path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\按日拆分\{}.xlsx'.format(datetime)
        df1.to_excel(path)