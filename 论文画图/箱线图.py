

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Heiti TC'
import numpy as np
# x = np.random.randint(10, 100, size=(5, 9)) # 随机生成5行9列 [10, 100]之间的数
x=np.array([[54.84,53.19,50.81,52.22,53.24,54.44],[56.05,55.24,53.23,52.82,52.41],[60.08,56.86,54.44,55.04,58.67]])
print(x) # 打印数据
x=x.T
plt.grid(True) # 显示网格
plt.boxplot(x, labels=['LSTM','多尺度CNN-LSTM','Proposed'],sym="r+", showmeans=True) # 绘制箱线图
plt.ylabel('准确率（%）')
plt.show() # 显示图片