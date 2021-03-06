import pandas as pd
import os
data_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据'
min_fif_path=os.path.join(data_dir,'沪深300-15min.csv')
daily_path=os.path.join(data_dir,'包含成交量的日频.xlsx')
min_fif_data=pd.read_csv(min_fif_path)
daily_data=pd.read_excel(daily_path,skiprows=3,header=None,names=['trade_index','trade_time','open','high','low','close','volume'],dtype=object)
min_fif_data['trade_time']=pd.to_datetime(min_fif_data['trade_time'])
daily_data['trade_time']=pd.to_datetime(daily_data['trade_time'])


# s1=daily_data.loc[(daily_data.index>=363)&(daily_data.index<1216),'volume'].tolist()
s1=min_fif_data.loc[(min_fif_data['trade_time']>=pd.to_datetime('2017-09-22 15:00:00'))&(min_fif_data['trade_time']<=pd.to_datetime('2021-04-12 14:45:00')),'volume'].tolist()
print(s1)
min_fif_data.loc[(min_fif_data['trade_time']>=pd.to_datetime('2017-09-25 9:45:00'))&(min_fif_data['trade_time']<=pd.to_datetime('2021-04-12 15:00:00')),'volume-1']=s1
print(daily_data)
# print(daily_data.loc[(daily_data.index>=364)&(daily_data.index<1216),'volume'])
# print(daily_data['volume_rate'])
min_fif_data=min_fif_data.loc[(min_fif_data['trade_time'] >='2017-09-25')&(min_fif_data['trade_time'] <'2021-04-13')]
print(daily_data)
min_fif_data.loc[:,"volume_rate"]=min_fif_data['volume']/min_fif_data['volume-1']-1
print(min_fif_data)
min_fif_data.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15min频成交量变化率.xlsx')
