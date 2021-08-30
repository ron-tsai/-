import pandas as pd
import os
dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础\数据区间试验'
wenben_dir='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'
new_dir='F:\\newstart\software\category\\tool\category\deal_with_data\数据二合为一'
daily_df=pd.read_excel(os.path.join(dir,'daily_data.xlsx'),dtype=object)

target_df=pd.read_excel(os.path.join(dir,'target.xlsx'))
guanzhu_df=pd.read_csv(os.path.join(wenben_dir,'沪深300.csv'),usecols=['时间','搜索指数'],encoding='gbk')
guanzhu_df.rename(columns={'时间':'trade_time','搜索指数':'search_index'},inplace=True)
print(daily_df)
guanzhu_df.loc[:,'trade_time']=pd.to_datetime(guanzhu_df['trade_time'])
print(guanzhu_df)
df=pd.merge(daily_df,guanzhu_df,on='trade_time',how='left')

df.to_excel(os.path.join(new_dir,'仅加入关注度.xlsx'),index=False)
