from Spyder import jobPymysql

sql_size = f"select workarea_text,sum(companysize_text) from jobTable group by workarea_text order by " \
           f"workarea_text; "
jobPymysql.cursor.execute(sql_size)
jobPymysql.conn.commit()
sql_tmp_data = jobPymysql.cursor.fetchall()
map_name = ['韶关市', '梅州市', '清远市', '河源市', '揭阳市', '潮州市', '汕头市', '肇庆市', '广州市', '惠州市', '佛山市', '东莞市', '云浮市', '汕尾市', '江门市',
            '中山市', '深圳市', '珠海市', '阳江市', '茂名市', '湛江市']
map_gz_name = ['从化区', '花都区', '增城区', '黄埔区', '白云区', '越秀区', '荔湾区', '天河区', '海珠区', '番禺区', '南沙区']
map_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
map_gzdata = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def mapdatalist():
    for x in range(len(sql_tmp_data)):
        for i in range(len(map_name)):
            if f'{sql_tmp_data[x][0][0: 2]}市' == map_name[i]:
                map_data[i] += sql_tmp_data[x][1] / 10000
    return map_data


def map_gzdatalist():
    for x in range(len(sql_tmp_data)):
        for i in range(len(map_gz_name)):
            if sql_tmp_data[x][0][0: 2] == '广州':
                if f'{sql_tmp_data[x][0][3: 6]}' == map_gz_name[i]:
                    map_gzdata[i] += sql_tmp_data[x][1] / 10000
    return map_gzdata
