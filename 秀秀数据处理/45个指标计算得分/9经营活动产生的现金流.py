import pandas as pd
df1=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\9\\9_1（5.7）.xls',dtype=object,names=['证券代码','截止日期','报表类型','经营现金净流量/营业总收入'])
df2=pd.read_excel('C:\\Users\Administrator\Desktop\秀秀数据\待做\\9\\9_2（5.7）.xls',dtype=object,names=['证券代码','截止日期x','报表类型','经营现金净流量/营业总收入'])


def get_ruisishujuzhuanhua(x):
    if x['截止日期x']==40268:
        return '2010-03-31'
    if x['截止日期x']==40359:
        return '2010-06-30'
    if x['截止日期x']==40451:
        return '2010-09-30'
    if x['截止日期x']==40543:
        return '2010-12-31'
    if x['截止日期x']==40633:
        return '2011-03-30'
    if x['截止日期x']==40724:
        return '2011-06-30'
    if x['截止日期x']==40816:
        return '2011-09-30'
    if x['截止日期x']==40908:
        return '2011-12-31'
    if x['截止日期x']==40999:
        return '2012-03-31'
    if x['截止日期x']==41090:
        return '2012-06-30'
    if x['截止日期x']==41182:
        return '2012-09-30'
    if x['截止日期x']==41274:
        return '2012-12-31'
    if x['截止日期x']==41364:
        return '2013-03-31'
    if x['截止日期x']==41455:
        return '2013-06-30'
    if x['截止日期x']==41547:
        return '2013-09-30'
    if x['截止日期x']==41639:
        return '2013-12-31'
    if x['截止日期x']==41729:
        return '2014-03-31'
    if x['截止日期x']==41820:
        return '2014-06-30'
    if x['截止日期x']==41912:
        return '2014-09-30'
    if x['截止日期x']==42004:
        return '2014-12-31'
    if x['截止日期x']==42094:
        return '2015-03-31'
    if x['截止日期x']==42185:
        return '2015-06-30'
    if x['截止日期x']==42277:
        return '2015-09-30'
    if x['截止日期x']==42369:
        return '2015-12-31'
    if x['截止日期x']==42460:
        return '2016-03-31'
    if x['截止日期x']==42551:
        return '2016-06-30'
    if x['截止日期x'] == 42643:
        return '2016-09-30'
    if x['截止日期x']==42735:
        return '2016-12-31'
    if x['截止日期x']==42825:
        return '2017-03-31'
    if x['截止日期x']==42916:
        return '2017-06-30'
    if x['截止日期x']==43008:
        return '2017-09-30'
    if x['截止日期x']==43100:
        return '2017-12-31'
    if x['截止日期x']==43190:
        return '2018-03-31'
    if x['截止日期x']==43281:
        return '2018-06-30'
    if x['截止日期x']==43373:
        return '2018-09-30'
    if x['截止日期x']==43465:
        return '2018-12-31'
    if x['截止日期x']==43555:
        return '2019-03-31'
    if x['截止日期x']==43646:
        return '2019-06-30'
    if x['截止日期x']==43738:
        return '2019-09-30'
    if x['截止日期x']==43830:
        return '2019-12-31'
    if x['截止日期x']==43921:
        return '2020-03-31'
    if x['截止日期x']==44012:
        return '2020-06-30'
    if x['截止日期x']==44104:
        return '2020-09-30'
    if x['截止日期x']==44196:
        return '2020-12-31'

df2.loc[:,'截止日期']=df2.apply(get_ruisishujuzhuanhua,axis=1)

df3=pd.concat([df1,df2],ignore_index=True,join='inner')
df3['截止月份']=pd.to_datetime(df3['截止日期']).dt.month
df3=df3.loc[df3['截止月份']==12]
print(df3)
df3.to_excel('C:\\Users\Administrator\Desktop\秀秀数据\处理完成\\9经营现金净流量 除  营业总收入.xlsx')