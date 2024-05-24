import random

import pyecharts.options as opts
from pyecharts.charts import Bar3D
from pyecharts.faker import Faker

# 定义变量
xdata = Faker.drinks
ydata = ['2019', '2020', '2021', '2022']
zdata = [random.randint(0, 100) for z in range(35)]
print(zdata)
data = [tuple(z) for z in zip(xdata * 7, ydata * 7, zdata)]

bar3d = (
    # 3D柱状图
    Bar3D(
        # 初始化配置项
        init_opts=opts.InitOpts(
            theme='white',  # 图表主题 white dark
        )
    )
        # 数据配置
        .add(
        series_name='销售数量',  # 系列名称
        data=data,  # 数值 格式为[(x,y,z),(x,y,z)]
        xaxis3d_opts=opts.Axis3DOpts(data=[list(z) for z in zip(xdata)]),  # X轴数据项 格式为[名称1, 名称2]
        yaxis3d_opts=opts.Axis3DOpts(data=[list(z) for z in zip(ydata)]),  # Y轴数据项 格式为[名称1, 名称2]
    )
        # !!!!全局配置项!!!!
        .set_global_opts(
        # 标题配置项
        title_opts=opts.TitleOpts(
            title="3D柱状图",  # 主标题
        ),
        # 视觉映射配置项
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,  # 是否显示视觉映射配置
        ),
    )
)
bar3d.render("test2.html")
