import pandas as pd
import os

path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始'

#日频数据处理
df1=pd.read_excel(os.path.join(path_dir,'step1：日频原数据拼接去重.xlsx'),dtype=object,col_index=False)
df1=df1.loc[:,~df1.columns.str.contains('Unnamed')]
df1['trade_time']=pd.to_datetime(df1['trade_time'])
df1.sort_values(by='trade_time',ascending=True,inplace=True)


total_df=df1.loc[(df1['trade_time']>=pd.to_datetime("2012-02-27"))&(df1['trade_time']<=pd.to_datetime("2021-04-12")),:]
#新建滞后一期列
s1=df1.loc[(df1['trade_time']>=pd.to_datetime('2012-02-24'))&(df1['trade_time']<pd.to_datetime('2021-04-12')),'volume'].tolist()

total_df.loc[(total_df['trade_time']>=pd.to_datetime('2012-02-27'))&(total_df['trade_time']<=pd.to_datetime('2021-04-12')),'volume-1']=s1
total_df.loc[:,"volume_rate"]=total_df['volume']/total_df['volume-1']-1
# print(total_df.shape)
# print(df.loc[(df['trade_time']>=pd.to_datetime("2019-03-22"))&(df['trade_time']<=pd.to_datetime("2019-05-22")),:])
# print(df.loc[(df['trade_time']>=pd.to_datetime("2019-03-22"))&(df['trade_time']<=pd.to_datetime("2019-05-22")),:].shape)
total_df.drop(['volume','volume-1'],axis=1,inplace=True)
print(total_df)
#切割数据集
daily_train_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2012-02-27"))&(total_df['trade_time']<=pd.to_datetime("2019-03-21")),:]
daily_val_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2019-03-22"))&(total_df['trade_time']<=pd.to_datetime("2020-03-31")),:]
daily_test_df=total_df.loc[(total_df['trade_time']>=pd.to_datetime("2020-04-01"))&(total_df['trade_time']<=pd.to_datetime("2021-04-12")),:]
save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\日频数据'
print(daily_train_df,daily_val_df,daily_test_df)
daily_train_df.to_excel((os.path.join(save_dir,'daily_train_data.xlsx')))
daily_val_df.to_excel((os.path.join(save_dir,'daily_val_data.xlsx')))
daily_test_df.to_excel((os.path.join(save_dir,'daily_test_data.xlsx')))







