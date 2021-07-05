import pandas as pd
import os
from matplotlib import pyplot as plt
import numpy as np

from keras.models import load_model
# load model from single file
model = load_model('初步模型[0-2].model')

##### 二、数据导入
finally_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\6比2比2\标准化后数据'

fif_train_df=pd.read_excel(os.path.join(finally_dir,'fif_train_data.xlsx'))
fif_val_df=pd.read_excel(os.path.join(finally_dir,'fif_val_data.xlsx'))
fif_test_df=pd.read_excel(os.path.join(finally_dir,'fif_test_data.xlsx'))

daily_train_df=pd.read_excel(os.path.join(finally_dir,'daily_train_data.xlsx'))
daily_val_df=pd.read_excel(os.path.join(finally_dir,'daily_val_data.xlsx'))
daily_test_df=pd.read_excel(os.path.join(finally_dir,'daily_test_data.xlsx'))

target_dir='F:\\newstart\software\category\\tool\category\deal_with_data\武汉金融数据\武汉金融复现：大数据量12年起始\\6比2比2\涨跌目标数据'
train_target_df=pd.read_excel(os.path.join(target_dir,'训练集target.xlsx'))
val_target_df=pd.read_excel(os.path.join(target_dir,'验证集target.xlsx'))
test_target_df=pd.read_excel(os.path.join(target_dir,'测试集target.xlsx'))



def val_tes_generator(input_data1,input_data2,target_data):
    while 1:
        rows = list(range(1, 421))
        samples1 = np.zeros((len(rows),
                             16,
                             5))
        samples2 = np.zeros((len(rows),
                             20,
                             5))

        targets = np.zeros((len(rows),))

        for j in rows:
            samples1[j - 1] = input_data1.loc[
                              (input_data1.index >= 320 + j * 16 - 32) & (input_data1.index < 320 + j * 16 - 16),
                              'open':]
            samples2[j - 1] = input_data2.loc[
                              (input_data2.index >= j -1) & (input_data2.index < 20 + j - 1),
                              'open':]

            targets[j - 1] = target_data.loc[target_data.index == j - 1, 'target']
        return ([samples1,samples2],targets)

val_gen=val_tes_generator(fif_val_df,daily_val_df,val_target_df)




test_gen=val_tes_generator(fif_test_df,daily_test_df,test_target_df)

print(test_gen[0])
print(test_gen[1])
loss,accuracy = model.evaluate(x=test_gen[0],y=test_gen[1])
print(loss,accuracy)
