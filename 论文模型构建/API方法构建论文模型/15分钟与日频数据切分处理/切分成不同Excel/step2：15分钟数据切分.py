import pandas as pd
import os
from matplotlib import pyplot as plt

data_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据'
min_fif_path=os.path.join(data_dir,'15min频成交量变化率.xlsx')
daily_path=os.path.join(data_dir,'日频成交量变化率.xlsx')


min_fif_data=pd.read_excel(min_fif_path)
min_fif_data['trade_time']=pd.to_datetime(min_fif_data['trade_time'])
min_fif_data=min_fif_data.loc[min_fif_data['trade_time'] >='2017-09-25']
print(min_fif_data)

min_fif_train_data=min_fif_data.loc[min_fif_data['trade_time']<'2020-06-16']

print("训练数据：",min_fif_train_data)
min_fif_train_data.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据初步处理\\15min_train_data.xlsx',index=False,columns=['trade_time','open','close','high','low','volume','money','volume-1','volume_rate'])
min_fif_val_data=min_fif_data.loc[(min_fif_data['trade_time']>='2020-06-16') & (min_fif_data['trade_time']<'2020-11-13'),:]
print("验证数据：",min_fif_val_data)
# min_fif_val_data.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据初步处理\\15min_val_data.xlsx',index=False,columns=['trade_time','open','close','high','low','volume','money'])
min_fif_val_data.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据初步处理\\15min_val_data.xlsx',index=False)

min_fif_test_data=min_fif_data.loc[min_fif_data['trade_time']>='2020-11-13']
print("测试数据：",min_fif_test_data)
# min_fif_test_data.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据初步处理\\15min_test_data.xlsx',index=False,columns=['trade_time','open','close','high','low','volume','money'])
min_fif_test_data.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据初步处理\\15min_test_data.xlsx',index=False)


# close_price=min_fif_data['close']
# date=min_fif_data.index
# plt.plot(date,close_price)
# plt.show()