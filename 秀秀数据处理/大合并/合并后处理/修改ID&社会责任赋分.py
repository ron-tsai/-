import pandas as pd
import os
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据'
path1='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\社会责任\合并'
df=pd.read_excel(os.path.join(path,'最终合并数据.xlsx'),dtype=object)
df.loc[:,'截止日期']=pd.to_datetime(df['截止日期']).dt.date


order=['ID','证券代码','截止日期','1股东大会出席股份比例(%)','2董事长与总经理兼任情况评分','3独立董事比例(%)','4董事会成员有无持股评分',
       '5高管是否持股评分','6机构投资者持股比例','7净资产收益率','9经营现金净流量/营业总收入','11资产负债率',
       '12总利润/总负债','14流动资产周转率','15总资产周转率A','16营业总收入增长率','17营业利润增长率','18归属于母公司净利润增长率',
       '19总资产增长率','22内部控制审计意见评分','23审计内部控制的会计师事务所排名评分','24内部控制缺陷及整改情况评分','27一季度报告及时性评分',
       '28二季度报告及时性评分','29三季度报告及时性评分','30年报告及时性评分','33第一大股东持股变化评分','39召开方式分数','40表决方式分数','是否公布社会责任报告']



df=df[order]
def get_socre(x):
    if x['是否公布社会责任报告']==1:
        return 100
df.loc[:,'是否公布社会责任报告']=df.apply(get_socre,axis=1)
df.loc[:,'ID']=df['ID']+1
df.fillna({'是否公布社会责任报告':0},inplace=True)
df.sort_values('ID',inplace=True)
df.to_excel(os.path.join(path,'最终合并数据111.xlsx'),index=False)