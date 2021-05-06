from keras.models import Model
from keras import layers
from keras import Input
import pandas as pd
from matplotlib import pyplot as plt
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









while 1:
    rows=list(range(1,641))
    samples1 = np.zeros((len(rows),
                       16,
                       4))
    samples2 = np.zeros((len(rows),
                       20,
                       4))

    targets=np.zeros((len(rows),))
    print(len(rows))
    for j in rows:

        samples1[j-1] = fif_train_df.loc[(fif_train_df.index >= 320+j*16-32) & (fif_train_df.index < 320+j*16-16), 'open':]
        # print(samples1[j-1])
        # samples2[j-1] = daily_train_df.loc[(daily_train_df.index >= 20+j-40) & (daily_train_df.index < 20+j-20), 'open':]
        print(daily_train_df.loc[(daily_train_df.index >= j-1) & (daily_train_df.index < 20+j-1), 'open':])
        targets[j-1] = train_target_df.loc[train_target_df.index == j-1, 'target']
    # print ({'output1': samples1, 'output2': samples2},targets)





