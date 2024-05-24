from pyecharts import options as opts
from pyecharts.charts import Map

import os

# 基础数据
quxian = ['鲤城区','丰泽区','洛江区','南安市', '晋江市','安溪县', '石狮市']

values3 = [63.89,63.89, 63.89,33.28, 23.32, 14.85, 12.20]

c = (
    Map()
        .add("泉州", [list(z) for z in zip(quxian, values3)], "泉州")
        .set_global_opts(
        title_opts=opts.TitleOpts(title="泉州地图"), visualmap_opts=opts.VisualMapOpts(max_=70)
    )
        .render()
)
# 打开html
os.system("render.html")

