import pandas as pd

import os
from datetime import timedelta
dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础\滞后过数据'
daily_df=pd.read_excel(os.path.join(dir,'daily_data.xlsx'),index_col='trade_time',parse_dates=True)
fif_df=pd.read_excel(os.path.join(dir,'fif_data.xlsx'),index_col='trade_time',parse_dates=True)
target=pd.read_excel(os.path.join(dir,'target.xlsx'),index_col='trade_time',parse_dates=True)
print(daily_df.loc[daily_df.index==pd.to_datetime('2020-03-05')].shift(1))
# print(fif_df)
# print(target)
#
# df = pd.DataFrame({'产品': ['A','B','C'],
#                    '数据1': [1, 4, 6],
#                    '数据2': [2, 5, 3]})
# print(df)
# print(df['数据1'].shift(1))
