### 项目说明：

本项目使用 Python 爬虫爬取 51job 广东应届毕业生招聘信息并存储进 mysql 数据库做毕业设计数据来源使用，且进行了数据预处理与分析，并使用可视化框架进行可视化，请按操作步骤配置本项目

### 操作步骤：

#### 一、爬虫，软件包Spyder

1、请根据MySQL 服务配置 jobPymysql.py初始化数据库 \
2、替换 cookie.txt内容，cookie 获取方式为：浏览器刷新 51job 页面然后 F12 网络筛选XHR，切换页数即可获取到 cookie \
3、按照开源项目https://github.com/jhao104/proxy_pool配置代理池 \
4、运行 jobSpyder.py进行爬虫并存储进 jobTable 表

##### 说明：也可使用本人爬取22-08-18到 22-10-18的sql数据:backup.sql，导入 sql 的方法如下：

1.`create database jobDB;` //新建一个库 \
2.`use jobDB;` //选中数据库 \
3.`set names utf8;` //设置编码模式为utf8 \
4.`source  <file>;` //导入sql文件，需要使用文件所在的路径./Data/backup22-11-21.sql

#### 二、预处理，软件包DataPretreatment

1、去重：运行reDuplicate.py匹配公司名+职位进行去重 \
2、格式转换：运行typeConversion.py对招聘人数与工资进行字符串正则表达式匹配并转换mysql字段类型

#### 三、数据分析，软件包DataAnalysis

1、运行 GBDT.py使用回归模型进行工资预测与模型评估

#### 四、可视化数据处理，软件包DataVisualization

1、DataPretreatment.reOutliers.dataoutliers异常值转换均值处理 \
2、招聘地址人数地图，数据筛选与统计

#### 五、数据可视化，软件包DataVisualization

1、DataVisualization.py生成 HTML 拼接，然后打开生成的 test.html 进行拼接配置保存生成配置json \
2、再次运行 DataVisualization.py应用拼接配置生成最终可视化 HTML，可搭配 web 框架进行前后端分离

### 警告

cache.txt为断点续传缓存文件，若存在爬虫续断，请勿删除或替换此文件 \
若提示更换 cookie 请先清除浏览器网站 cookie，然后按照步骤(一、2) 获取 cookie，然后输入框输入 cookie 回车即可 