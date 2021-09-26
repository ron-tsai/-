import pandas as pd
import os
import numpy as np
path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.4'
df=pd.read_excel(os.path.join(path,'【3】9月4日数据pandas删除.xlsx'),dtype=object,index=False)
df0=pd.DataFrame({'ID':[],'证券代码':[],'截止日期':[],'1股东大会出席股份比例(%)':[],'2董事长与总经理兼任情况评分':[],'4董事会成员有无持股评分':[],'5高管是否持股评分':[],'7净资产收益率':[],'11资产负债率':[],'12总利润/总负债':[],'14流动资产周转率':[],'15总资产周转率A':[],'16营业总收入增长率':[],'17营业利润增长率':[],'18归属于母公司净利润增长率':[],'19总资产增长率':[],'22内部控制审计意见评分':[],'23审计内部控制的会计师事务所排名评分':[],'24内部控制缺陷及整改情况评分':[],'30年报告及时性评分':[],'33第一大股东持股变化评分':[],'39召开方式分数':[],'40表决方式分数':[],'是否公布社会责任报告':[]})

g=df.groupby('ID')
for name,group in g:
    g_df = pd.DataFrame(group)

    list_1=g_df.columns
    for name in list_1[3:]:
        mean=g_df[name].mean()
        g_df.loc[:,name]=g_df[name].fillna(mean)
        print(g_df[name].fillna(mean))
    df0 = pd.concat([df0, g_df], join='inner')
    print(df0.shape)

df0.to_excel(os.path.join(path, '【4】9月4日数据pandas填充.xlsx'), index=False)



