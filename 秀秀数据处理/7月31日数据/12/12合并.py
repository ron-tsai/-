import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\\12'
df1=pd.read_excel(os.path.join(path,'负债合计-.xlsx'),dtype=object,index=False)
df2=pd.read_excel(os.path.join(path,'总利润-.xlsx'),dtype=object,index=False)

df_merge=pd.merge(df1,df2,on=['截止日期','证券代码','报表类型'],how='outer')

df_merge.loc[:,'总利润/总负债']=df_merge['利润总额']/df_merge['负债合计']


df_merge.to_excel(os.path.join(path,'12利润负债表.xlsx'))

