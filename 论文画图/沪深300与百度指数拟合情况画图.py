import pandas as pd
import os
import matplotlib.pyplot as plt

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

new_dir='F:\\newstart\software\category\\tool\category\deal_with_data\数据二合为一'
mix_file='666777.xlsx'
df=pd.read_excel(os.path.join(new_dir,mix_file))
y1=df['close'].to_list()
y2=df['search_index'].to_list()
x=df['trade_time'].to_list()

plt.figure()
plt.plot(x,y2, color='darkorange')
plt.ylabel('百度指数')

plt.xlabel('年份')

plt.twinx()
plt.plot(x,y1, color='b')
plt.plot( color='navy', linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])


plt.ylabel('沪深300指数')
plt.title('沪深300指数收盘价与百度指数图')
plt.legend(loc="best")
plt.show()


