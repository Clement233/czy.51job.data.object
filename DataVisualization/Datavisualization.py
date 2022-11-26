import os

from bs4 import BeautifulSoup
from pyecharts.charts import Page
from pyecharts.components import Table

import DataVisualization.bar
import DataVisualization.funnel
import DataVisualization.map
import DataVisualization.pie
import DataVisualization.wordcloud

page = Page(layout=Page.DraggablePageLayout, page_title="51job广东应届毕业生招聘信息")
table = Table()
table.add(headers=["51job广东应届毕业生招聘信息数据大屏"], rows=[], attributes={
    "align": "center",
    "border": False,
    "padding": "2px",
    "style": "width:1350px; height:50px; font-size:25px; color:#C0C0C0;"
})
# 在页面中添加图表
page.add(
    table,
    DataVisualization.bar.size_bar(),
    DataVisualization.map.map_gd(),
    DataVisualization.pie.pie_gz(),
    DataVisualization.funnel.funnel_10(),
    DataVisualization.wordcloud.wordcloud()
)

# 保存大屏拖拽配置，请先打开 test.html--save_config生成拖拽配置
if os.path.isfile("chart_config.json"):
    page.save_resize_html('test.html', cfg_file='chart_config.json', dest='51job广东应届毕业生招聘信息.html')
    with open(os.path.join(os.path.abspath("."), "51job广东应届毕业生招聘信息.html"), 'r+', encoding="utf8") as html:
        html_bf = BeautifulSoup(html, "lxml")
        body = html_bf.find("body")
        body["style"] = """
        background: url("https://clubimg.club.vmall.com/data/attachment/forum/201810/27/081757dekscvamsgy4wuel.jpg"); 
        background-size: cover; 
        content: ""; 
        position: absolute;
        width: 100%; 
        height: 100%; 
        backdrop-filter: blur(20px);
        """
        html_new = str(html_bf)
        html.seek(0, 0)
        html.truncate()
        html.write(html_new)
        html.close()
else:
    page.render('test.html')
