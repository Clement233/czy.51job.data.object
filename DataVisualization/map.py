from pyecharts import options as opts
from pyecharts.charts import Map

import DataAnalysis.mapData


def map_gd():
    c = Map()
    c.add("广东招聘人数(单位：/w)",
          [list(z) for z in zip(DataAnalysis.mapData.map_name, DataAnalysis.mapData.mapdatalist())],
          "广东")
    c.add("广州招聘人数(单位：/w)",
          [list(z) for z in zip(DataAnalysis.mapData.map_gz_name, DataAnalysis.mapData.map_gzdatalist())],
          "广州")
    c.set_global_opts(
        legend_opts=opts.LegendOpts(selected_mode='single'),
        title_opts=opts.TitleOpts(title="广东应届毕业生招聘人数地图"),
        visualmap_opts=opts.VisualMapOpts()
    )
    # c.render("map.html")
    return c
