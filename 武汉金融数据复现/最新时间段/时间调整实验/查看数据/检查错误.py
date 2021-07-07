import pandas as pd
import os

path_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\标准化处理数据基础\数据区间试验'
df = pd.read_excel(os.path.join(path_dir, 'target.xlsx'), dtype=object,index=False)
df = df.loc[:, ~df.columns.str.contains('Unnamed')]
df['trade_time'] = pd.to_datetime(df['trade_time'])


print(df.loc[df.duplicated()==True])