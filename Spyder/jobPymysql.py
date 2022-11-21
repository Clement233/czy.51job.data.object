import pymysql

# 定义 MySQL 与 pymasql 接口
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='12345678',
    charset='utf8'
)
# 获取游标
cursor = conn.cursor()
# 创建数据库
sql_create = "create database if not exists jobDB"
cursor.execute(sql_create)
# 创建数据表
sql_use = 'use jobDB'
cursor.execute(sql_use)
sql_table = "create table if not exists jobTable(" \
            "`id` int not null AUTO_INCREMENT, " \
            "`jobid` int, " \
            "`coid` int, " \
            "`job_href` text, " \
            "`job_name` varchar(50), " \
            "`company_href` text, " \
            "`company_name` text, " \
            "`providesalary_text` varchar(50), " \
            "`workarea_text` varchar(50), " \
            "`companytype_text` varchar(50), " \
            "`issuedate` DATETIME, " \
            "`jobwelf` text, " \
            "`attribute_text` varchar(50), " \
            "`companysize_text` varchar(50), " \
            "`companyind_text` text," \
            "primary key (`id`)," \
            "unique (`jobid`))" \
            "ENGINE=InnoDB DEFAULT CHARSET=utf8;"
cursor.execute(sql_table)
conn.commit()
print("已完成 mysql 初始化。")
