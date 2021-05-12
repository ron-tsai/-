import pandas as pd
import os
import numpy as np
path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始'



#15分钟频数据处理
df2=pd.read_csv(os.path.join(path_dir,'沪深300-15min.csv'),dtype=object)
# print(df2)
df2=df2.loc[:,~df2.columns.str.contains('Unnamed')]
df2['trade_time']=pd.to_datetime(df2['trade_time'])
df2.sort_values(by='trade_time',ascending=True,inplace=True)


total_df2=df2.loc[(df2['trade_time']>=pd.to_datetime("2012-02-27"))&(df2['trade_time']<=pd.to_datetime("2021-04-13")),:]
#新建滞后一期列
s2=df2.loc[(df2['trade_time']>=pd.to_datetime('2012-02-24 15:00:00'))&(df2['trade_time']<=pd.to_datetime('2021-04-12 14:45:00')),'volume'].tolist()
print(s2)
print(total_df2.loc[(total_df2['trade_time']>=pd.to_datetime('2012-02-27 9:45:00'))&(total_df2['trade_time']<=pd.to_datetime('2021-04-12 15:00:00')),:])
total_df2.loc[(total_df2['trade_time']>=pd.to_datetime('2012-02-27 9:45:00'))&(total_df2['trade_time']<=pd.to_datetime('2021-04-12 15:00:00')),'volume-1']=s2
total_df2.drop('money',axis=1,inplace=True)
print(total_df2)

total_df2['volume'] = total_df2['volume'].astype(np.float64)
total_df2['volume-1'] = total_df2['volume-1'].astype(np.float64)
total_df2.loc[:,"volume_rate"]=total_df2['volume']/total_df2['volume-1']-1


# total_df2.loc[total_df2['volume-1']>0,'volume_rate']=total_df2['volume']/total_df2['volume-1']-1
# print(total_df.shape)
# print(df.loc[(df['trade_time']>=pd.to_datetime("2019-03-22"))&(df['trade_time']<=pd.to_datetime("2019-05-22")),:])
# print(df.loc[(df['trade_time']>=pd.to_datetime("2019-03-22"))&(df['trade_time']<=pd.to_datetime("2019-05-22")),:].shape)
#删除无用列
total_df2.drop(['volume','volume-1'],axis=1,inplace=True)
#将volume_rate中缺失值填满
total_df2.replace([np.inf, -np.inf],np.nan,inplace=True)
total_df2.fillna({'volume_rate':0},inplace=True)

#切割数据集
fif_train_df=total_df2.loc[(total_df2['trade_time']>=pd.to_datetime("2012-02-27"))&(total_df2['trade_time']<pd.to_datetime("2019-03-22")),:]
fif_val_df=total_df2.loc[(total_df2['trade_time']>=pd.to_datetime("2019-03-22"))&(total_df2['trade_time']<pd.to_datetime("2020-04-01")),:]
fif_test_df=total_df2.loc[(total_df2['trade_time']>=pd.to_datetime("2020-04-01"))&(total_df2['trade_time']<pd.to_datetime("2021-04-13")),:]

print(fif_train_df,fif_val_df,fif_test_df)
save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\15分钟频数据'

fif_train_df.to_excel((os.path.join(save_dir,'fif_train_data.xlsx')))
fif_val_df.to_excel((os.path.join(save_dir,'fif_val_data.xlsx')))
fif_test_df.to_excel((os.path.join(save_dir,'fif_test_data.xlsx')))