from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import os

# 基础数据
quxian = ['安溪县', '德化县', '南安市', '永春县', '晋江市', '惠安县', '洛江区', '泉港区',
          '石狮市', '金门县','丰泽区','鲤城区','']

values3 = [3057.28, 2232, 2036, 1456.87, 649, 489.42, 374.81, 341, 159.9, 153.06,108,53.74]

c = (
    Map()
        .add("泉州", [list(z) for z in zip(quxian, values3)], "泉州")
        .set_global_opts(
        title_opts=opts.TitleOpts(title="泉州地图"), visualmap_opts=opts.VisualMapOpts(max_=3500)
    )
        .render()
)
# 打开html
os.system("render.html")

