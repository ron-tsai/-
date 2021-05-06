import pandas as pd
import os
from matplotlib import pyplot as plt

data_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据'
min_fif_path=os.path.join(data_dir,'15min频成交量变化率.xlsx')
daily_path=os.path.join(data_dir,'日频成交量变化率.xlsx')


daily_data=pd.read_excel(daily_path,skiprows=1,header=None,names=['trade_index','trade_time','open','high','low','close','volume','volume-1','volume_rate'],dtype=object)
daily_data['trade_time']=pd.to_datetime(daily_data['trade_time'])
daily_data=daily_data.loc[(daily_data['trade_time'] >='2017-09-25')&(daily_data['trade_time'] <'2021-04-13')]
print(daily_data)

daily_train_data=daily_data.loc[daily_data['trade_time']<'2020-06-16']

print("训练数据：",daily_train_data)
daily_train_data.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\日频数据初步处理\\daily_train_data.xlsx',index=False)
daily_val_data=daily_data.loc[(daily_data['trade_time']>='2020-06-16') & (daily_data['trade_time']<'2020-11-13'),:]
print("验证数据：",daily_val_data)
daily_val_data.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\日频数据初步处理\\daily_val_data.xlsx',index=False)

daily_test_data=daily_data.loc[daily_data['trade_time']>='2020-11-13']
print("测试数据：",daily_test_data)
daily_test_data.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\日频数据初步处理\\daily_test_data.xlsx',index=False)


# close_price=min_fif_data['close']
# date=min_fif_data.index
# plt.plot(date,close_price)
# plt.show()