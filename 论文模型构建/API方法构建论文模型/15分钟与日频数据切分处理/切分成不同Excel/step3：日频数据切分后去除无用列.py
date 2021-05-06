import pandas as pd
train_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\日频数据初步处理\\daily_train_data.xlsx')
val_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\日频数据初步处理\\daily_val_data.xlsx')
test_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\日频数据初步处理\\daily_test_data.xlsx')

train_df=train_df[['trade_time','open','close','high','low','volume_rate']]
print(train_df)
val_df=val_df[['trade_time','open','close','high','low','volume_rate']]
test_df=test_df[['trade_time','open','close','high','low','volume_rate']]

train_df.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\日频数据\\daily_train_data.xlsx')
val_df.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\日频数据\\daily_val_data.xlsx')
test_df.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\日频数据\\daily_test_data.xlsx')