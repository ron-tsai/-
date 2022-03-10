import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif']=['Microsoft YaHei']  #显示中文标签,处理中文乱码问题
# plt.rcParams['axes.unicode_minus']=False  #坐标轴负号的处理
plt.rcParams['font.family'] = 'Heiti TC'
plt.axes(aspect='equal')  #将横、纵坐标轴标准化处理，确保饼图是一个正圆，否则为椭圆

#构造数据
edu = [1.8,8.10,2.70,1.80,48.65,3.60,33.33]

labels = ['其他','私有化','转板上市','证券置换','经营业绩不达标','重大信息披露违法','吸收合并']
explode = [0.1, 0.1, 0.1, 0.1,0.1,0.1,0.1]  #生成数据，用于凸显大专学历人群
colors = ['#e3f0ff','#fad9c1', '#63ace5', '#03396c', '#3b5998', '#adcbe3']  #自定义颜色

plt.pie(x=edu,  #绘图数据
        explode=explode, #指定饼图某些部分的突出显示，即呈现爆炸式
        labels=labels,  #添加教育水平标签
        colors=colors,
        autopct='%.2f%%',  #设置百分比的格式，这里保留两位小数
        pctdistance=0.8,  #设置百分比标签与圆心的距离
        labeldistance=1.1,  #设置教育水平标签与圆心的距离
        startangle=180,  #设置饼图的初始角度
        radius=1.2,  #设置饼图的半径
        counterclock=False,  #是否逆时针，这里设置为顺时针方向
        wedgeprops={'linewidth':1.5, 'edgecolor':'green'},  #设置饼图内外边界的属性值
        textprops={'fontsize':12, },  #设置文本标签的属性值
        )

#添加图标题
# plt.legend( frameon=False)
# plt.title('上市公司退市原因分布')
#显示图形
plt.show()

