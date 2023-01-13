import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(10, 100, size=(5, 9)) # 随机生成5行9列 [10, 100]之间的数
print(x) # 打印数据
plt.grid(True) # 显示网格
plt.boxplot(x, labels=list("ABCDEFGHI"), sym="r+", showmeans=True) # 绘制箱线图
plt.show() # 显示图片