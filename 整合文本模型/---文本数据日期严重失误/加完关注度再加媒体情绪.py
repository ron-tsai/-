import pandas as pd
import os
dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础\数据区间试验'
wenben_dir='F:\\newstart\software\category\\tool\category\deal_with_data\新闻来源筛选完成\情感赋分\每日均值'
new_dir='F:\\newstart\software\category\\tool\category\deal_with_data\数据二合为一'
daily_df=pd.read_excel(os.path.join(new_dir,'仅加入关注度.xlsx'),dtype=object)
metiqingxu_df=pd.read_excel(os.path.join(wenben_dir,'合并.xlsx'),dtype=object)

df=pd.merge(daily_df,metiqingxu_df,on='trade_time',how='left')

df.to_excel(os.path.join(new_dir,'加了关注度再加媒体情绪.xlsx'),index=False)