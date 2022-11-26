import pyecharts.options as opts
from pyecharts.charts import WordCloud

import DataAnalysis.wordcloudData

data = DataAnalysis.wordcloudData.wcdata()


def wordcloud():
    c = (
        WordCloud()
            .add(series_name="招聘福利关键词分析", data_pair=data, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="招聘福利关键词分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return c
