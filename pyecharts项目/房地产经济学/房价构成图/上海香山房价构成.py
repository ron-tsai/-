from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

x_data = ["拆迁安置补偿费", "规划设计和报建费", "大市政和基础设施费", "公共配套设施费", "建安工程费", "税", "其他费用",
          "利息", "净利润"]
y_data = [3346.01, 140.29, 1035.22, 128.15, 1758.63,843.4,69.83,781.87,152.02]

c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(x_data, y_data)],
        radius=["40%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="北京法华寺南里小区房价构成"))
    .render("pie_rich_label.html")
)

