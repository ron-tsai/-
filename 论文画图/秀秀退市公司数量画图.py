import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Heiti TC'


num_list = [5,3,3,6,1,7,1,5,7,11,16,19]
year_list=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
plt.bar(range(len(num_list)), num_list,tick_label=year_list,label='2010-2021年每年A股退市公司数量')
plt.legend(loc="upper left", fontsize=10)
def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        plt.bar.annotate('{}'.format(height), # put the detail data
                    xy=(rect.get_x() + rect.get_width() / 2, height), # get the center location.
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
def auto_text(rects):
    for rect in rects:
        plt.bar.text(rect.get_x(), rect.get_height(), rect.get_height(), ha='left', va='bottom')
auto_text(rect1)

plt.show()
