import pandas as pd
import os


data_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\8比1比1'

daily_path=os.path.join(data_dir,'step1：日频原数据拼接去重.xlsx')


daily_data=pd.read_excel(daily_path)
daily_data['trade_time']=pd.to_datetime(daily_data['trade_time'])
daily_data=daily_data.loc[(daily_data['trade_time'] >='2012-02-27')&(daily_data['trade_time'] <'2021-04-13')]

daily_data['trade_time']=pd.to_datetime(daily_data['trade_time']).dt.date

train_target_start=pd.to_datetime('2012-02-27')
train_target_end=pd.to_datetime('2012-03-26')

print(daily_data.loc[(daily_data['trade_time'] >=train_target_start)&(daily_data['trade_time'] <train_target_end)])


