
import pyecharts.options as opts
from pyecharts.charts import Bar3D


# 定义变量
xdata = ['北京','上海','广州','深圳','福建','全国']
ydata = ['2017','2018','2019', '2020','2021']
zdata = [32140.00,34142.89,35905.00,37665.00,40526.00,
         23804.00,26890.08,30677.00,33798.00,36102.00,
         17633.00,20013.60,22363.00,25056.00,28034.00,
         47936.00,54132.44,55797.00,56829.00,58593.00,
         9746.00,10589.18,10748.00,11348.00,11779.00,
         7892.00,8726.00,9310.00,9860.00,10139.00]
Year=5
City=6
xdata_ =  [ele for ele in xdata for i in range(Year)] #让xdata变成[北京、北京、北京……]
print(xdata_)
print(ydata *5)
data = [tuple(z) for z in zip(xdata_ , ydata*City, zdata)] #ydata*K 让ydata变为[17，18，……17，18]
print(data)
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
        series_name='房价',  # 系列名称
        data=data,  # 数值 格式为[(x,y,z),(x,y,z)]
        xaxis3d_opts=opts.Axis3DOpts(data=[list(z) for z in zip(xdata)]),  # X轴数据项 格式为[名称1, 名称2]
        yaxis3d_opts=opts.Axis3DOpts(data=[list(z) for z in zip(ydata)]),  # Y轴数据项 格式为[名称1, 名称2]
    )
        # !!!!全局配置项!!!!
        .set_global_opts(
        # 标题配置项

        title_opts=opts.TitleOpts(
            title="北上广深福建房价变化3D柱状图",  # 主标题
        ),
        # 视觉映射配置项
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,  # 是否显示视觉映射配置
            max_=60000,
            min_=9000,
        ),
    )
)
bar3d.render("test1.html")
