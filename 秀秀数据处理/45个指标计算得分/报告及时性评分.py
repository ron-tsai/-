import pandas as pd
df=pd.read_excel('C:\\Users\Administrator\Desktop\\27 28 29 30.xlsx',skiprows=3,names=['证券代码','证券简称','报告类型','会计截止日期','报告公布日期'],dtype=object)

print(df)

df['报告公布日期']=pd.to_datetime(df['报告公布日期'])
siyue=pd.to_datetime('04-30')
bayue=pd.to_datetime('08-31')
shiyue=pd.to_datetime('10-31')
def get_gongbujishixing(x):
    if (x['报告类型'==1])&(x['报告公布日期']<=siyue):
        return 100
    if (x['报告类型'==1])&(x['报告公布日期']>siyue):
        return 0
    if (x['报告类型'==2])&(x['报告公布日期']<=bayue):
        return 100
    if (x['报告类型'==2])&(x['报告公布日期']>bayue):
        return 0
    if (x['报告类型'==3])&(x['报告公布日期']<=shiyue):
        return 100
    if (x['报告类型'==3])&(x['报告公布日期']>shiyue):
        return 0
    if (x['报告类型'==4])&(x['报告公布日期']<=siyue):
        return 100
    if (x['报告类型'==4])&(x['报告公布日期']>siyue):
        return 0

df.loc[:,'评分']=df.apply(get_gongbujishixing,axis=1)

df.to_excel('C:\\Users\Administrator\Desktop\\报告及时性打分.xlsx')