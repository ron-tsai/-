from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd

l1= pd.period_range('1986','2021',freq='Y').strftime("%Y").values.tolist()

print(l1)
l2=[1991,2506,3536,3985,4400,5128,13566,26027,31486,33482,21269,21286,24378,25762,27303,
    29552,32618,37123,59242,56290,58710,62518,87562,80407,85218,88419,89859,91444,94197,
    93426,94948,95897,97937,99544,103262,105434]
bar = (
    Bar()
    .add_xaxis(l1)
    .add_yaxis("开发企业数量", l2)
    .set_global_opts(title_opts=opts.TitleOpts(title="1986年—2021年开发企业数量", subtitle="资料来源：《中国统计年鉴2022》"))
)
# 生成render.html查看表格
bar.render()
