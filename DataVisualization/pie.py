from pyecharts import options as opts
from pyecharts.charts import Pie

import DataAnalysis.mapData


def pie_gz():
    c = (
        Pie().add(
            "",
            [list(z) for z in zip(DataAnalysis.mapData.map_gz_name, map(float, DataAnalysis.mapData.map_gzdatalist()))],
            radius=["10%", "55%"],  # 设置饼图环形区间上下限
            rosetype="radius",  # 设置半径分数据
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="广州招聘人数（单位/w）"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
        ).set_series_opts(
            label_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    )
    return c
