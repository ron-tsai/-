
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Heiti TC'

fig, ax = plt.subplots()

n_groups = 5 #列数

data1=[53.15,59.68,51.51,55.10,56]
data2=[56.98,59.72,71.87,65.18,56]

bar_width = 0.4 #每条柱状的宽度
index=np.arange(n_groups) #刻度索引

#保证横坐标的刻度位于连个柱状之间
rects1 = ax.bar(index-1/2*bar_width, data1, bar_width,label='多尺度CNN-LSTM') #绘制柱状1
rects2 = ax.bar(index+1/2*bar_width, data2, bar_width,label='Proposed') #绘制柱状2

plt.xticks(index,['准确率','精确率','召回率','F1值','AUC']) #用指定的字符串表示横坐标的刻度

ax.legend() #绘制图例（即右上角的方框）

fig.tight_layout()
plt.show()

