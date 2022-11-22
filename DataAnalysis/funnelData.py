from Spyder import jobPymysql

sql = "select company_name,count(company_name) coun,company_href from jobTable group by company_name,company_href " \
      "order by coun desc limit 10; "
jobPymysql.cursor.execute(sql)
jobPymysql.conn.commit()
sql_tmp_data = jobPymysql.cursor.fetchall()


def company_name_data():
    a = []
    for e in range(len(sql_tmp_data)):
        a.append(sql_tmp_data[e][0])
    return a


def count_company_name_data():
    a = []
    for e in range(len(sql_tmp_data)):
        a.append(sql_tmp_data[e][1])
    return a


def company_href_data():
    a = []
    for e in range(len(sql_tmp_data)):
        a.append(sql_tmp_data[e][2])
    return a
