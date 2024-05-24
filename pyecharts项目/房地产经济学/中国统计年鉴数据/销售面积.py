from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd

l1= pd.period_range('1987','2021',freq='Y').strftime("%Y").values.tolist()

print(l1)
l2=[2697.24,2927.33,2855.36,2871.54,3025.46,4288.86,6687.91,7230.35,7905.94,7900.41,9010.17,12185.33,
    14556.50,18637.13,22411.90,26808.29,33717.60,38231.60,55486.22,61857.07,77345.72,65969.83,94755.00,
    104764.65,109366.75,111303.65,130550.59,120648.54,128494.97,157348.53,169407.82,171464.60,171557.87,
    176086.22,179433.41]
bar = (
    Bar()
    .add_xaxis(l1)
    .add_yaxis("销售面积", l2)
    .set_global_opts(title_opts=opts.TitleOpts(title="1987年—2021年商品房销售面积", subtitle="资料来源：《中国统计年鉴2022》"))
)
# 生成render.html查看表格
bar.render()
