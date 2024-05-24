from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import os

# 基础数据
quxian = ['安溪县', '德化县', '南安市', '晋江市', '惠安县', '洛江区', '泉港区',
          '石狮市', '丰泽区','鲤城区','']

values3 = [15675, 13007, 9765,17314,10244,17297 ,7147 ,11627,22294,21966]

c = (
    Map()
        .add("泉州", [list(z) for z in zip(quxian, values3)], "泉州")
        .set_global_opts(
        title_opts=opts.TitleOpts(title="泉州地图"), visualmap_opts=opts.VisualMapOpts(max_=25000)
    )
        .render()
)
# 打开html
os.system("render.html")

