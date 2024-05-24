from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import os

# 基础数据
city = ['福州市', '莆田市', '泉州市', '厦门市', '漳州市', '龙岩市', '三明市', '南平市', '宁德市']

values2 = [11788, 3895, 10864, 1515, 12608, 19052, 23191, 26312, 13644]

c = (
    Map()
        .add("福建", [list(z) for z in zip(city, values2)], "福建")
        .set_global_opts(
        title_opts=opts.TitleOpts(title="福建地图"), visualmap_opts=opts.VisualMapOpts(max_=30000)
    )
        .render()
)
# 打开html
os.system("render.html")

