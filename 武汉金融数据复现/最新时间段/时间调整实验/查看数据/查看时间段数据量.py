import pandas as pd
import os
from datetime import timedelta
path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础'
df = pd.read_excel(os.path.join(path_dir, '至7月日频数据.xlsx'), dtype=object, col_index=False)
df = df.loc[:, ~df.columns.str.contains('Unnamed')]
df['trade_time'] = pd.to_datetime(df['trade_time'])
print(df.index)
start='2013-01-08'
# start='2021-04-13'
end='2021-07-05'
print(df.loc[(df['trade_time']>=pd.to_datetime(start)+timedelta(days=1))&(df['trade_time']<=pd.to_datetime(end))].shape)