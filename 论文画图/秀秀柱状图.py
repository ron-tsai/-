import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Heiti TC'

def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height), # put the detail data
                    xy=(rect.get_x() + rect.get_width() / 2, height), # get the center location.
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def auto_text(rects):
    for rect in rects:
        ax.text(rect.get_x(), rect.get_height(), rect.get_height(), ha='left', va='bottom')


labels = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
# men_means = [20, 34, 30, 35, 27]
women_means = [5,3,3,6,1,7,1,5,7,11,16,19]

index = np.arange(len(labels))
width = 0.8

fig, ax = plt.subplots()
# rect1 = ax.bar(index - width / 2, men_means, color ='lightcoral', width=width, label ='Men')
rect2 = ax.bar(index , women_means, width=width, label ='A股退市公司数量')

# ax.set_title('Scores by gender')
ax.set_xticks(ticks=index)
ax.set_xticklabels(labels)
ax.set_ylabel('2010-2021年每年A股退市公司数量')

# ax.set_ylim(0, 50)
# auto_label(rect1)
# auto_label(rect2)
# auto_text(rect1)
auto_text(rect2)

ax.legend(loc='upper left', frameon=False)
fig.tight_layout()
plt.savefig('2.tif', dpi=300)
plt.show()