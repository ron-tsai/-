import pandas as pd

df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\副本2020year.xlsx',skiprows=3,header=None,names=['ID','date','title','content','source'])

df.set_index(pd.to_datetime(df['date']),inplace=True) ###本来就无分秒无需'.dt.date'

df.drop(['date','ID'],axis=1,inplace=True)

for i in range(12):

    begin='2020-{}'.format(i+1)
    # end='2020-{}-01'.format(i+2)
    df1=df.loc[begin]
    df1.set_index(pd.to_datetime(df1.index,format='%d/%b/%Y') ,inplace=True)  ###有分秒需'.dt.date'
    file_path='F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年{}月.xlsx'.format(i+1)
    df1.to_excel(file_path)



# df1=df.loc['2020-01-01':'2020-02-01']
# df2=df.loc['2020-02-01':'2020-03-01']
# df3=df.loc['2020-03-01':'2020-04-01']
# df4=df.loc['2020-04-01':'2020-05-01']
# df5=df.loc['2020-05-01':'2020-06-01']
# df6=df.loc['2020-06-01':'2020-07-01']
# df7=df.loc['2020-07-01':'2020-08-01']
# df8=df.loc['2020-08-01':'2020-09-01']
# df9=df.loc['2020-09-01':'2020-10-01']
# df10=df.loc['2020-10-01':'2020-11-01']
# df11=df.loc['2020-11-01':'2020-12-01']
# df12=df.loc['2020-12-01':]
#
# df1.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年1月.xlsx')
# df2.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年2月.xlsx')
# df3.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年3月.xlsx')
# df4.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年4月.xlsx')
# df5.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年5月.xlsx')
# df6.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年6月.xlsx')
# df7.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年7月.xlsx')
# df8.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年8月.xlsx')
# df9.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年9月.xlsx')
# df10.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年10月.xlsx')
# df11.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年11月.xlsx')
# df12.to_excel('F:\\newstart\software\category\\tool\category\deal_with_data\国泰安\新闻聚合\月频数据\\2020年12月.xlsx')
#



