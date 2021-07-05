import pandas as pd
import os


data_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\8比1比1'

daily_path=os.path.join(data_dir,'step1：日频原数据拼接去重.xlsx')


daily_data=pd.read_excel(daily_path)
daily_data['trade_time']=pd.to_datetime(daily_data['trade_time'])
daily_data=daily_data.loc[(daily_data['trade_time'] >='2012-02-27')&(daily_data['trade_time'] <'2021-04-13')]

daily_data['trade_time']=pd.to_datetime(daily_data['trade_time']).dt.date

train_target_start=pd.to_datetime('2012-03-26')
train_target_end=pd.to_datetime('2021-04-12')
date_list=[]
close_list=[]
for idx in daily_data['trade_time']:
    if (idx>=train_target_start)&(idx<=train_target_end):

        train_target_df=daily_data.loc[daily_data['trade_time']==idx,:]
        time=train_target_df['trade_time'].values.tolist()
        close=train_target_df['close'].values.tolist()
        date_list=date_list+time

        close_list=close_list+close


print(date_list)
print(close_list)
last_close=2552.94 #2012-03-23
target_list=[]
for idx,value in enumerate(close_list):
    if value < last_close:
        target_list=target_list+[0]
        last_close=value
    else:
        target_list=target_list+[1]
        last_close=value
print(target_list)
target=target_list
close=close_list
trade_time=date_list
df=pd.DataFrame({'trade_time':trade_time,'close':close,'target':target})
save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础\滞后过数据'
df.to_excel(os.path.join(save_dir,'target.xlsx'),index=False)

