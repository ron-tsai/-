from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import os

# 基础数据
value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr = ["China", "Canada", "Brazil", "Russia", "United States"]

data = []
for index in range(len(attr)):
    city_ionfo=[attr[index],value[index]]
    data.append(city_ionfo)

c = (
    Map()
    .add("世界地图",data, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界地图示例"),
        visualmap_opts=opts.VisualMapOpts(max_=200),

    )
    .render()
)

# 打开html
os.system("render.html")
