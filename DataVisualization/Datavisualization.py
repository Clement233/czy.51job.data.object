from pyecharts.charts import Page

import DataVisualization.bar
import DataVisualization.map

page = Page(layout=Page.DraggablePageLayout, page_title="51job广东应届毕业生招聘信息")

# 在页面中添加图表
page.add(
    DataVisualization.bar.size_bar(),
    DataVisualization.map.map_gd(), )

page.render('test.html')
# 保存大屏拖拽配置，请先打开 test.html--save_config生成拖拽配置
if open('chart_config.json') is not None:
    page.save_resize_html('test.html', cfg_file='chart_config.json', dest='51job广东应届毕业生招聘信息.html')
