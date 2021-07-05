import pandas as pd
import os

path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\8比1比1'

#日频数据处理
df1=pd.read_excel(os.path.join(path_dir,'step1：日频原数据拼接去重.xlsx'),dtype=object,col_index=False)
df1=df1.loc[:,~df1.columns.str.contains('Unnamed')]
df1['trade_time']=pd.to_datetime(df1['trade_time'])
df1.sort_values(by='trade_time',ascending=True,inplace=True)


total_df=df1.loc[(df1['trade_time']>=pd.to_datetime("2012-01-01"))&(df1['trade_time']<=pd.to_datetime("2019-09-30")),:]
#新建滞后一期列

save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\8比1比1\日频数据'
total_df.to_excel(os.path.join(save_dir,'total_daily_data.xlsx'))
