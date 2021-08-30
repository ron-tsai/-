import pandas as pd
import os

save_path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\社会责任\合并'
df=pd.read_excel(os.path.join(save_path,'社会责任报告merge.xlsx'),dtype=object)
def get_f(x):
    if x['社会责任报告名称']:
        return 1
df.loc[:,'是否公布社会责任报告']=df.apply(get_f,axis=1)

df1=df.loc[(df['截止日期']<=pd.to_datetime('2020-12-31'))&(df['截止日期']>=pd.to_datetime('2010-12-31')),:]
df1=df1.loc[:,~df1.columns.str.contains('Unnamed')]
df1.drop_duplicates(subset=None,keep='first',inplace=True)
df1.to_excel(os.path.join(save_path,'社会责任报告只差股票代码筛选.xlsx'),columns=['证券代码','截止日期','是否公布社会责任报告'],index=False)
