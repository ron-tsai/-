import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\18归属母公司股东的净利润同比增长率.xlsx',dtype=object,index_col=False)
print(df["证券代码"].value_counts().shape)


