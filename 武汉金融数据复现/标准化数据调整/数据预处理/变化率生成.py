# import pandas as pd
# import numpy as np
# import os
# dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础'
# daily_df=pd.read_excel(os.path.join(dir,'step1：日频原数据拼接去重.xlsx'))
# fif_df=pd.read_csv(os.path.join(dir,'沪深300-15min.csv'),dtype=object)
#
#
# def rate(df):
#     df = df.loc[:, ~df.columns.str.contains('Unnamed')]
#     df['trade_time'] = pd.to_datetime(df['trade_time'])
#     df.sort_values(by='trade_time', ascending=True, inplace=True)
#
#     # 新建滞后一期列
#     s1 = df.loc[(df.index>=1) & (df.index<-1), 'volume'].to_list()
#     s2 = df.loc[(df.index>1) & (df.index<=-1), 'volume'].to_list()
#     s3=map(lambda(a,b):a/b,zip(s1,s2))
#     s3=s1/s2
#     print(s3)
#     print(s2)
#     return s3
#     # df.drop(1,axis=0)
#     # print(df)
#     # df.loc[(total_df2['trade_time'] >= pd.to_datetime('2012-02-27 9:45:00')) & (
#     # total_df2['trade_time'] <= pd.to_datetime('2021-04-12 15:00:00')), 'volume-1'] = s2
#     # total_df2.drop('money', axis=1, inplace=True)
#     # print(total_df2)
#     #
#     # total_df2['volume'] = total_df2['volume'].astype(np.float64)
#     # total_df2['volume-1'] = total_df2['volume-1'].astype(np.float64)
#     # total_df2.loc[:, "volume_rate"] = total_df2['volume'] / total_df2['volume-1'] - 1
#     #
#     # total_df2.drop(['volume', 'volume-1'], axis=1, inplace=True)
#     # # 将volume_rate中缺失值填满
#     # total_df2.replace([np.inf, -np.inf], np.nan, inplace=True)
#     # total_df2.fillna({'volume_rate': 0}, inplace=True)
# rate(daily_df)


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


save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础\滞后过数据'


total_df2.to_excel((os.path.join(save_dir,'fif_data.xlsx')),index=False)





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

total_df.drop(['volume','volume-1'],axis=1,inplace=True)
print(total_df)



total_df.to_excel((os.path.join(save_dir,'daily_data.xlsx')),index=False)







