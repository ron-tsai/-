import pandas as pd
import os
import matplotlib.pyplot as plt

new_dir='F:\\newstart\software\category\\tool\category\deal_with_data\数据二合为一'
mix_file='666777.xlsx'
df=pd.read_excel(os.path.join(new_dir,mix_file))
y1=df['close'].to_list()
y2=df['sector_score'].to_list()
x=df['trade_time'].to_list()

plt.figure()
plt.plot(x,y2, color='darkorange')
plt.twinx()
plt.plot(x,y1, color='b')
plt.plot( color='navy', linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()