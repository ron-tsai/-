from datetime import timedelta
import pandas as pd
import os
import numpy as np
path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\\武汉金融数据\标准化处理数据基础'

#15分钟频数据处理
def fif_pre(dir,start,end):

    df=pd.read_csv(os.path.join(dir,'沪深300.csv'),dtype=object)
    # print(df2)
    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df['trade_time']=pd.to_datetime(df['trade_time'])
    df.sort_values(by='trade_time',ascending=True,inplace=True)


    total_df=df.loc[(df['trade_time']>=pd.to_datetime(start))&(df['trade_time']<=pd.to_datetime(end+ ' 15:00:00')),:]
    print(total_df)
    #新建滞后一期列
    s=total_df.loc[(total_df['trade_time']>=pd.to_datetime(start + ' 15:00:00'))&(total_df['trade_time']<=pd.to_datetime(end+' 14:45:00')),'volume'].tolist()
    print('s:',len(s))
    print('s:', s)
    print(total_df.loc[(total_df['trade_time']>=pd.to_datetime(start+' 9:45:00')+timedelta(days=1))&(total_df['trade_time']<=pd.to_datetime(end+' 15:00:00')),:])
    total_df.loc[(total_df['trade_time']>=pd.to_datetime(start+' 9:45:00')+timedelta(days=1))&(total_df['trade_time']<=pd.to_datetime(end+' 15:00:00')),'volume-1']=s
    total_df.drop('money',axis=1,inplace=True)
    print('total_df:',total_df)

    total_df['volume'] = total_df['volume'].astype(np.float64)
    total_df['volume-1'] = total_df['volume-1'].astype(np.float64)
    total_df.loc[:,"volume_rate"]=total_df['volume']/total_df['volume-1']-1


    #删除无用列
    total_df.drop(['volume','volume-1'],axis=1,inplace=True)
    #将volume_rate中缺失值填满
    total_df.replace([np.inf, -np.inf],np.nan,inplace=True)
    total_df.fillna({'volume_rate':0},inplace=True)

    total_df=total_df.loc[(df['trade_time']>=pd.to_datetime(start)+timedelta(days=1))&(total_df['trade_time']<=pd.to_datetime(end+ ' 15:00:00')),:]



    total_df.to_excel((os.path.join(save_dir,'fif_data.xlsx')),index=False)
#日频数据处理
def daily_pre(dir,start,end):
    df=pd.read_excel(os.path.join(dir,'至7月日频数据.xlsx'),dtype=object,col_index=False)
    df=df.loc[:,~df.columns.str.contains('Unnamed')]
    df['trade_time']=pd.to_datetime(df['trade_time'])
    df.sort_values(by='trade_time',ascending=True,inplace=True)


    total_df=df.loc[(df['trade_time']>=pd.to_datetime(start))&(df['trade_time']<=pd.to_datetime(end)),:]
    #新建滞后一期列
    s=df.loc[(df['trade_time']>=pd.to_datetime(start))&(df['trade_time']<pd.to_datetime(end)),'volume'].tolist()

    total_df.loc[(total_df['trade_time']>=pd.to_datetime(start)+timedelta(days=1))&(total_df['trade_time']<=pd.to_datetime(end)),'volume-1']=s
    total_df.loc[:,"volume_rate"]=total_df['volume']/total_df['volume-1']-1

    total_df.drop(['volume','volume-1'],axis=1,inplace=True)
    print(total_df)


    total_df=total_df.loc[(df['trade_time']>=pd.to_datetime(start)+timedelta(days=1))&(df['trade_time']<=pd.to_datetime(end)),:]
    total_df.to_excel((os.path.join(save_dir,'daily_data.xlsx')),index=False)

def get_target(x):
    if x['close']>=x['close-1']:
        return 1
    if x['close']<x['close-1']:
        return 0
def target_pre(dir, start, end):
    total_df=pd.read_excel(os.path.join(dir,'至7月日频数据.xlsx'),dtype=object,col_index=False)
    total_df['trade_time'] = pd.to_datetime(total_df['trade_time'])
    s = total_df.loc[
        (total_df['trade_time'] >= pd.to_datetime(start)) & (total_df['trade_time'] < pd.to_datetime(end)), 'close'].tolist()

    total_df.loc[(total_df['trade_time'] >= pd.to_datetime(start) + timedelta(days=1)) & (
    total_df['trade_time'] <= pd.to_datetime(end)), 'close-1'] = s
    print(len(s))

    total_df = total_df.loc[(total_df['trade_time'] >= pd.to_datetime(start) + timedelta(days=1)) & (total_df['trade_time'] <= pd.to_datetime(end)), :]
    total_df.loc[:,'target']=total_df.apply(get_target,axis=1)
    print(total_df)
    df=total_df[['trade_time','close','target']]
    print(df)
    df.to_excel((os.path.join(save_dir, 'target.xlsx')), index=False)






save_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础\\数据区间试验'
start='2012-01-05'
end='2019-09-30'
fif_pre(path_dir,start,end)
daily_pre(path_dir,start,end)

target_pre(path_dir,start,end)

