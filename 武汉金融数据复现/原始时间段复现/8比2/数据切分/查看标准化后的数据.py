import pandas as pd
import os
daily_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\8比2\日频'
fif_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融原时间数据复现\8比2\\15分钟频'
daily_df=pd.read_excel(os.path.join(daily_dir,'train_norm.xlsx'))
fif_df=pd.read_excel(os.path.join(fif_dir,'train_norm.xlsx'))

print(daily_df['open'].mean())