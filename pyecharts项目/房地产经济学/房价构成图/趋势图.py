import pyecharts.options as opts
from pyecharts.charts import Line
x=['1890','1990','1910','1920','1930','1940','1950','1960','1970','1980','1987']
y1=[1.2690,1.5964,2.0256,2.4352,2.9905,3.4949,4.2857,5.8326,6.8672,8.8207,10.2652]
y2=[4.93,4.76,4.54,4.34,4.11,3.77,3.37,3.33,3.14,2.76,2.66]
line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="住房单元（千万套）",y_axis=y1, is_smooth=True)
    .add_yaxis(series_name="每户人数",y_axis=y2, is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="1890-1987年美国住房单元总量"))
)
line.render("1890-1987年美国住房单元总量.html")