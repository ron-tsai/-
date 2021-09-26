import pandas as pd
import os

path='C:\\Users\Administrator\Desktop\秀秀数据\待做\\731数据\查看数据\9.4'
df=pd.read_excel(os.path.join(path,'【5】9月4日数据pandas修改ID.xlsx'),dtype=object,index=False)
def norm(df):
    x=df.copy()
    yi_mean_value = df['1股东大会出席股份比例(%)'].mean(axis=0)
    er_mean_value = df['2董事长与总经理兼任情况评分'].mean(axis=0)
    si_mean_value = df['4董事会成员有无持股评分'].mean(axis=0)
    wu_mean_value = df['5高管是否持股评分'].mean()
    qi_mean_value = df['7净资产收益率'].mean()
    shiyi_mean_value = df['11资产负债率'].mean()
    shier_mean_value = df['12总利润/总负债'].mean(axis=0)
    shisi_mean_value = df['14流动资产周转率'].mean()
    shiwu_mean_value = df['15总资产周转率A'].mean()
    shiliu_mean_value = df['16营业总收入增长率'].mean()
    shiqi_mean_value = df['17营业利润增长率'].mean(axis=0)
    shiba_mean_value = df['18归属于母公司净利润增长率'].mean()
    shijiu_mean_value = df['19总资产增长率'].mean()
    erer_mean_value = df['22内部控制审计意见评分'].mean()
    ersan_mean_value = df['23审计内部控制的会计师事务所排名评分'].mean(axis=0)
    ersi_mean_value = df['24内部控制缺陷及整改情况评分'].mean()
    # erqi_mean_value = df['27一季度报告及时性评分'].mean()
    # erba_mean_value = df['28二季度报告及时性评分'].mean()
    # erjiu_mean_value = df['29三季度报告及时性评分'].mean()
    sanshi_mean_value = df['30年报告及时性评分'].mean()
    sansan_mean_value = df['33第一大股东持股变化评分'].mean()
    sanjiu_mean_value = df['39召开方式分数'].mean()
    sishi_mean_value = df['40表决方式分数'].mean()
    siyi_mean_value = df['是否公布社会责任报告'].mean()

    yi_std_value = df['1股东大会出席股份比例(%)'].std(axis=0)
    er_std_value = df['2董事长与总经理兼任情况评分'].std(axis=0)
    si_std_value = df['4董事会成员有无持股评分'].std(axis=0)
    wu_std_value = df['5高管是否持股评分'].std()
    qi_std_value = df['7净资产收益率'].std()
    shiyi_std_value = df['11资产负债率'].std()
    shier_std_value = df['12总利润/总负债'].std(axis=0)
    shisi_std_value = df['14流动资产周转率'].std()
    shiwu_std_value = df['15总资产周转率A'].std()
    shiliu_std_value = df['16营业总收入增长率'].std()
    shiqi_std_value = df['17营业利润增长率'].std(axis=0)
    shiba_std_value = df['18归属于母公司净利润增长率'].std()
    shijiu_std_value = df['19总资产增长率'].std()
    erer_std_value = df['22内部控制审计意见评分'].std()
    ersan_std_value = df['23审计内部控制的会计师事务所排名评分'].std(axis=0)
    ersi_std_value = df['24内部控制缺陷及整改情况评分'].std()
    # erqi_std_value = df['27一季度报告及时性评分'].std()
    # erba_std_value = df['28二季度报告及时性评分'].std()
    # erjiu_std_value = df['29三季度报告及时性评分'].std()
    sanshi_std_value = df['30年报告及时性评分'].std()
    sansan_std_value = df['33第一大股东持股变化评分'].std()
    sanjiu_std_value = df['39召开方式分数'].std()
    sishi_std_value = df['40表决方式分数'].std()
    siyi_std_value=df['是否公布社会责任报告'].std()

    x['1股东大会出席股份比例(%)']=(df['1股东大会出席股份比例(%)']-yi_mean_value)/yi_std_value
    x['2董事长与总经理兼任情况评分']=(df['2董事长与总经理兼任情况评分']-er_mean_value)/er_std_value
    x['4董事会成员有无持股评分'] = (df['4董事会成员有无持股评分'] - si_mean_value) / si_std_value
    x['5高管是否持股评分'] =  (df['5高管是否持股评分'] - wu_mean_value) / wu_std_value
    x['7净资产收益率'] =  (df['7净资产收益率'] - qi_mean_value) / qi_std_value
    x['11资产负债率'] = (df['11资产负债率'] - shiyi_mean_value) / shiyi_std_value
    x['12总利润/总负债'] = (df['12总利润/总负债'] - shier_mean_value) / shier_std_value
    x['14流动资产周转率'] = (df['14流动资产周转率'] - shisi_mean_value) / shisi_std_value
    x['15总资产周转率A'] = (df['15总资产周转率A'] - shiwu_mean_value) / shiwu_std_value
    x['16营业总收入增长率'] = (df['16营业总收入增长率'] - shiliu_mean_value) / shiliu_std_value
    x['17营业利润增长率'] = (df['17营业利润增长率'] - shiqi_mean_value) / shiqi_std_value
    x['18归属于母公司净利润增长率'] = (df['18归属于母公司净利润增长率'] - shiba_mean_value) / shiba_std_value
    x['19总资产增长率'] = (df['19总资产增长率'] - shijiu_mean_value) / shijiu_std_value
    x['22内部控制审计意见评分'] = (df['22内部控制审计意见评分'] - erer_mean_value) / erer_std_value
    x['23审计内部控制的会计师事务所排名评分'] = (df['23审计内部控制的会计师事务所排名评分'] - ersan_mean_value) / ersan_std_value
    x['24内部控制缺陷及整改情况评分'] = (df['24内部控制缺陷及整改情况评分'] - ersi_mean_value) / ersi_std_value
    # x['27一季度报告及时性评分'] = (df['27一季度报告及时性评分'] - erqi_mean_value) / erqi_std_value
    # x['28二季度报告及时性评分'] = (df['28二季度报告及时性评分'] - erba_mean_value) / erba_std_value
    # x['29三季度报告及时性评分'] = (df['29三季度报告及时性评分'] - erjiu_mean_value) / erjiu_std_value
    x['30年报告及时性评分'] = (df['30年报告及时性评分'] - sanshi_mean_value) / sanshi_std_value
    x['33第一大股东持股变化评分'] = (df['33第一大股东持股变化评分'] - sansan_mean_value) / sansan_std_value
    x['39召开方式分数'] = (df['39召开方式分数'] - sanjiu_mean_value) / sanjiu_std_value
    x['40表决方式分数'] = (df['40表决方式分数'] - sishi_mean_value) / sishi_std_value
    x['是否公布社会责任报告']=(df['是否公布社会责任报告'] - siyi_mean_value) / siyi_std_value
    df=x
    return df

df1=norm(df)
df1.to_excel(os.path.join(path, '【6】9月4日数据pandas无量纲化处理.xlsx'), index=False)