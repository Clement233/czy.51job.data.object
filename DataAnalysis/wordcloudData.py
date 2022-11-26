import re

from Spyder import jobPymysql

sql = "select jobwelf from jobTable;"
jobPymysql.cursor.execute(sql)
jobPymysql.conn.commit()
sql_tmp_data = jobPymysql.cursor.fetchall()


def wcdata():
    data = []
    for i in range(len(sql_tmp_data)):
        data.extend(re.split(r"\s+", sql_tmp_data[i][0]))

    dictdata = {}
    for key in data:
        dictdata[key] = dictdata.get(key, 0) + 1
    return list(dictdata.items())
