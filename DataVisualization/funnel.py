import pyecharts.options as opts
from pyecharts.charts import Funnel

import DataAnalysis.funnelData


def funnel_10():
    x_data = DataAnalysis.funnelData.company_name_data()
    y_data = DataAnalysis.funnelData.count_company_name_data()
    urldata = DataAnalysis.funnelData.company_href_data()
    data = [[x_data[i], y_data[i]] for i in range(len(x_data))]
    c = (
        Funnel(init_opts=opts.InitOpts(chart_id='chart1')
               ).add(
            series_name="",
            data_pair=data,
            gap=2,
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="招聘人数 : {c}，点击可进入该公司主页"),
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
            itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="前十公司招聘需求漏斗图"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%")
        ).add_js_funcs(
            f"chart_chart1.on('click', function(params){{"
            f"if (params.dataIndex == 0) {{window.location.href='{urldata[0]}';}}"
            f"else if (params.dataIndex == 1) {{window.location.href='{urldata[1]}';}}"
            f"else if (params.dataIndex == 2) {{window.location.href='{urldata[2]}';}}"
            f"else if (params.dataIndex == 3) {{window.location.href='{urldata[3]}';}}"
            f"else if (params.dataIndex == 4) {{window.location.href='{urldata[4]}';}}"
            f"else if (params.dataIndex == 5) {{window.location.href='{urldata[5]}';}}"
            f"else if (params.dataIndex == 6) {{window.location.href='{urldata[6]}';}}"
            f"else if (params.dataIndex == 7) {{window.location.href='{urldata[7]}';}}"
            f"else if (params.dataIndex == 8) {{window.location.href='{urldata[8]}';}}"
            f"else if (params.dataIndex == 9) {{window.location.href='{urldata[9]}';}}"
            f"}});"
        )
    )
    return c
