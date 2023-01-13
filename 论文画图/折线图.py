# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Heiti TC'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
x = ['5日', '10日', '15日', '20日']
y1 = [53.23, 56.98, 54.44, 52.42]
y2 = [56.57, 59.72, 60.16, 55.44]
y3 = [71.22, 71.87, 55.40, 76.98]
y4 = [63.06, 65.18, 57.68, 64.46]
y5=[52,56,54,54]
plt.plot(x, y1, marker='*', ms=10, label="准确率")
plt.plot(x, y2, marker='*', ms=10, label="精确率")
plt.plot(x, y3, marker='*', ms=10, label="召回率")
plt.plot(x, y4, marker='*', ms=10, label="F1值")
plt.plot(x, y5, marker='*', ms=10, label="AUC")
plt.xticks(rotation=0)
# plt.xlabel("发布日期")
plt.ylabel("百分比（%）")
# plt.title("80小说网活跃度")
plt.legend(loc='best')
# 在折线图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for y in [y1, y2, y3, y4]:
    for x1, yy in zip(x, y):
        plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=10, rotation=0)
plt.savefig("a.jpg")
plt.show()

