
import pandas as pd
import numpy as np



fif_train_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_train_data.xlsx')
fif_val_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_val_data.xlsx')
fif_test_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\\15分钟数据\\15min_test_data.xlsx')

daily_train_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\日频数据\daily_train_data.xlsx')
daily_val_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\日频数据\daily_val_data.xlsx')
daily_test_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\日频数据\daily_test_data.xlsx')

train_target_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\每日涨跌数据\\训练集target.xlsx')
val_target_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\每日涨跌数据\\验证集target.xlsx')
test_target_df=pd.read_excel('F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\每日涨跌数据\\测试集target.xlsx')

rows=list(range(1,2))
# print(fif_train_df.loc[fif_train_df.index==320])
# print(fif_train_df.loc[(fif_train_df.index >= 320+1*16-32) & (fif_train_df.index < 320+1*16-16), ])
# print(train_target_df)
# print(train_target_df.loc[train_target_df.index == 0])

# for j,row in enumerate(rows):
#     print(j)
#     print(row)
print(daily_train_df.loc[(daily_train_df.index >= 20+1*20-40) & (daily_train_df.index < 20+1*20-20), ])

samples2 = np.zeros((len(rows),
                             20,
                             4))
print(samples2[0])