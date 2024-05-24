from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd

l1= ['1998',  '2000', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

print(l1)
l2=[2513.30,3935.44,17576.13,20825.96,29889.12,25068.18,44355.17,52721.24,58588.86,64455.79,
    81428.28,76292.41,87280.84,117627.05,133701.31,149614.42,159725.12,173612.66,181929.95]
bar = (
    Bar()
    .add_xaxis(l1)
    .add_yaxis("销售额（亿元）", l2)
    .set_global_opts(title_opts=opts.TitleOpts(title="我国房地产销售额", subtitle="资料来源：《中国统计年鉴2022》"))
)
# 生成render.html查看表格
bar.render()
