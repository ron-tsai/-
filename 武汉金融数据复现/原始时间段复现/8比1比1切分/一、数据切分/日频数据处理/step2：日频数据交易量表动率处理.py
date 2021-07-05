import pandas as pd
import os

path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\\6比2比2\日频数据'
#日频数据处理
total_df=pd.read_excel(os.path.join(path_dir,'total_daily_data.xlsx'),dtype=object,col_index=False)




#新建滞后一期列
s1=total_df.loc[(total_df['trade_time']>=pd.to_datetime('2012-01-06'))&(total_df['trade_time']<pd.to_datetime('2019-09-30')),'volume'].tolist()
print(len(s1))
total_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime('2012-01-05'))&(total_df['trade_time']<=pd.to_datetime('2019-09-30')),:]
total_df=total_df.loc[:,~total_df.columns.str.contains('Unnamed')]

total_df.loc[(total_df['trade_time']>=pd.to_datetime('2012-01-05'))&(total_df['trade_time']<=pd.to_datetime('2019-09-30')),'volume-1']=s1
total_df.loc[:,"volume_rate"]=total_df['volume']/total_df['volume-1']-1
# print(total_df.shape)
# print(df.loc[(df['trade_time']>=pd.to_datetime("2019-03-22"))&(df['trade_time']<=pd.to_datetime("2019-05-22")),:])
# print(df.loc[(df['trade_time']>=pd.to_datetime("2019-03-22"))&(df['trade_time']<=pd.to_datetime("2019-05-22")),:].shape)
total_df.drop(['volume','volume-1'],axis=1,inplace=True)
# print(total_df)
#切割数据集
daily_train_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2012-01-05"))&(total_df['trade_time']<=pd.to_datetime("2016-08-08")),:]
print(daily_train_df)
daily_val_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2016-08-10"))&(total_df['trade_time']<=pd.to_datetime("2018-02-22")),:]
# print(daily_val_df)
daily_test_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2018-02-23"))&(total_df['trade_time']<=pd.to_datetime("2019-09-30")),:]
print(daily_test_df)
save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现'
print(daily_train_df,daily_val_df,daily_test_df)
# daily_train_df.to_excel((os.path.join(save_dir,'daily_train_data.xlsx')))
# daily_val_df.to_excel((os.path.join(save_dir,'daily_val_data.xlsx')))
# daily_test_df.to_excel((os.path.join(save_dir,'daily_test_data.xlsx')))







