import pandas as pd
import os


data_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始'

daily_path=os.path.join(data_dir,'step1：日频原数据拼接去重.xlsx')


daily_data=pd.read_excel(daily_path,dtype=object)
daily_data=daily_data.loc[:,~daily_data.columns.str.contains('Unnamed')]
daily_data['trade_time']=pd.to_datetime(daily_data['trade_time'])
daily_data=daily_data.loc[(daily_data['trade_time'] >='2012-01-05')&(daily_data['trade_time'] <='2019-09-30')]

daily_data['trade_time']=pd.to_datetime(daily_data['trade_time']).dt.date

print(daily_data.loc[(daily_data['trade_time'] >=pd.to_datetime('2012-01-05'))&(daily_data['trade_time'] <=pd.to_datetime('2019-09-30'))])


date_list=[]
close_list=[]
for idx in daily_data['trade_time']:
    train_target_start = pd.to_datetime('2012-02-09')
    train_target_end = pd.to_datetime('2019-09-30')
    if (idx>=train_target_start)&(idx<=train_target_end):

        train_target_df=daily_data.loc[daily_data['trade_time']==idx,:]
        time=train_target_df['trade_time'].values.tolist()
        close=train_target_df['close'].values.tolist()
        date_list=date_list+time

        close_list=close_list+close


print(date_list)
print(close_list)
last_close=2528.24 #2012-02-08
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
print(df)
train_target=df.loc[(df['trade_time']>pd.to_datetime('2012-02-09'))&(df['trade_time']<pd.to_datetime('2018-02-14'))]
test_target=df.loc[(df['trade_time']>pd.to_datetime('2018-03-22'))&(df['trade_time']<pd.to_datetime('2019-09-30'))]
# print(daily_data.loc[(daily_data['trade_time'] >=pd.to_datetime('2018-03-22'))&(daily_data['trade_time'] <=pd.to_datetime('2019-09-30'))])
save_path='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\8比2\每日涨跌'
df.to_excel(os.path.join(save_path,'train_target.xlsx'))
df.to_excel(os.path.join(save_path,'test_target.xlsx'))


