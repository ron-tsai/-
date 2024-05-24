import pyecharts.options as opts
from pyecharts.charts import Pie

import os
c = (
    Pie()
        .add(
        "",
        [list(z) for z in zip(['大泉州市区','南安市','南安市', '晋江市','安溪县', '石狮市'],
                              [ 63.89,33.28,33.28, 23.32, 14.85, 12.20])],
        center=["20%", "30%"],  # 位置
        radius=[60, 80],  # 每个饼图内外圈的大小
    )
        .add(
        "",
        [list(z) for z in zip(["奇幻", "其他"], [40, 60])],
        center=["55%", "30%"],
        radius=[60, 80],
    )
        .add(
        "",
        [list(z) for z in zip(["爱情", "其他"], [24, 76])],
        center=["20%", "70%"],
        radius=[60, 80],
    )
        .add(
        "",
        [list(z) for z in zip(["惊悚", "其他"], [11, 89])],
        center=["55%", "70%"],
        radius=[60, 80],
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-多饼图基本示例"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        )
    )
.render('没错.html')
)


