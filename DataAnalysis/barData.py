from Spyder import jobPymysql


def bardata_list(x):
    data = []
    for i in range(0, 30, 3):
        if bardata(x)[i] + bardata(x)[i + 1] + bardata(x)[i + 2] == 0:
            data.append(0)
        else:
            data.append(bardata(x)[i] + bardata(x)[i + 1] + bardata(x)[i + 2])
    if bardata(x)[30] == 0:
        data.append(0)
    else:
        data.append(bardata(x)[30])
    return data


def bardate():
    date = []
    for i in range(1, 31, 3):
        date.append(f'{i}-{i + 2}日')
    date.append('31日')
    return date


def bardata(month):
    sql_size = f"select DATE_FORMAT(issuedate,'%d') date,sum(companysize_text) from jobTable where month(issuedate) " \
               f"in ({month}) group by DATE_FORMAT(issuedate,'%d') order by date; "
    jobPymysql.cursor.execute(sql_size)
    jobPymysql.conn.commit()
    sql_tmp_data = jobPymysql.cursor.fetchall()
    size_data = []
    for e in range(1, 32):
        a = False
        for j in sql_tmp_data:
            if e == int(j[0]):
                size_data.append(int(j[1]))
                a = True
                continue
        if a:
            continue
        size_data.append(0)
    return size_data
