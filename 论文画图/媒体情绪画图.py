import pandas as pd
import os
import matplotlib.pyplot as plt



path='F:\\newstart\software\category\\tool\category\deal_with_data\\1\合并数据'
df1=pd.read_csv(os.path.join(path,'1.csv'),usecols=['news_id','pub_date','overall_senti_score_adjust'],parse_dates=True)
df2=pd.read_csv(os.path.join(path,'2.csv'),usecols=['news_id','pub_date','overall_senti_score_adjust'],parse_dates=True)
df3=pd.concat([df1,df2],ignore_index=True,join='inner')

df3.loc[:,'pub_date']=pd.to_datetime(df3['pub_date'])
print(df3)
beg=pd.to_datetime('2013-01-09')
end=pd.to_datetime('2021-07-03')
df4=df3.loc[(df3['pub_date']>=beg)&(df3['pub_date']<=end),:]

g=df4.groupby('pub_date')['overall_senti_score_adjust'].mean()
g_df=pd.DataFrame(g).reset_index()
print(g_df)

y3=g_df['overall_senti_score_adjust'].to_list()



plt.show()



new_dir='F:\\newstart\software\category\\tool\category\deal_with_data\数据二合为一'
mix_file='666777.xlsx'
df=pd.read_excel(os.path.join(new_dir,mix_file))
y1=df['close'].to_list()
y2=df['search_index'].to_list()
x=df['trade_time'].to_list()

plt.figure()
plt.plot(x,y3, color='darkorange')
plt.twinx()
plt.plot(x,y1, color='b')
plt.plot( color='navy', linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()