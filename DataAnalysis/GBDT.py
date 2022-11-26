import re

import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

from Spyder import jobPymysql

sql_tmp = "CREATE TABLE if not exists GBDTtable " \
          "(`id` int not null AUTO_INCREMENT," \
          "`gz` float," \
          "`gslx` varchar(50)," \
          "`gzlx` text," \
          "`gzdz-xl` varchar(50)," \
          "`gzdz` varchar(50)," \
          "`xl` varchar(50)," \
          "primary key (`id`));"
jobPymysql.cursor.execute(sql_tmp)
jobPymysql.conn.commit()


def insert_table():
    sql_insert = "insert into GBDTtable(" \
                 "`gz`,`gslx`,`gzlx`,`gzdz-xl`) " \
                 "SELECT providesalary_text 'gz'," \
                 "companytype_text 'gslx'," \
                 "companyind_text 'gzlx'," \
                 "attribute_text 'gzdz-xl'" \
                 "FROM jobTable; "
    jobPymysql.cursor.execute(sql_insert)
    jobPymysql.conn.commit()


def get_dummies_job(lie):
    sql_fenglei = f"select `{lie}`, count(`{lie}`) `{lie}分类` from GBDTtable group by `{lie}` order by `{lie}分类` desc;"
    jobPymysql.cursor.execute(sql_fenglei)
    jobPymysql.conn.commit()
    tmp_fenglei = jobPymysql.cursor.fetchall()
    fenglei_dict = {}
    for i in range(len(tmp_fenglei)):
        fenglei_dict[tmp_fenglei[i][0]] = i

    sql_dummies = f"select `{lie}` from GBDTtable;"
    jobPymysql.cursor.execute(sql_dummies)
    jobPymysql.conn.commit()
    tmp_list = []
    tmp = jobPymysql.cursor.fetchall()
    for e in range(len(tmp)):
        tmp_list.append(tmp[e][0])
    dummies_list = []
    for z in tmp_list:
        for a, b in fenglei_dict.items():
            if a == z:
                z = z.replace(a, f'{b}')
                dummies_list.append(int(z))
    return dummies_list


def dataPre():
    sql_xdata = "select `gzdz-xl` from GBDTtable;"
    jobPymysql.cursor.execute(sql_xdata)
    jobPymysql.conn.commit()
    tmp_xdata = jobPymysql.cursor.fetchall()
    data = []
    for i in range(len(tmp_xdata)):
        data.append(re.split(r",", tmp_xdata[i][0]))
    x1data = []
    for e in range(len(data)):
        x1data.append(data[e][0])
    x2data = []
    for e in range(len(data)):
        x2data.append(data[e][-1])
    for x in range(len(x1data)):
        jobPymysql.cursor.execute(
            f"update GBDTtable set `gzdz`='{x1data[x]}',`xl`= '{x2data[x]}' where `id` = {x + 1};")
    jobPymysql.cursor.close()
    jobPymysql.conn.commit()
    jobPymysql.conn.close()


def y_data():
    sql_ydata = "select `gz` from GBDTtable;"
    jobPymysql.cursor.execute(sql_ydata)
    jobPymysql.conn.commit()
    tmp_ydata = jobPymysql.cursor.fetchall()
    y_data_list = []
    for i in range(len(tmp_ydata)):
        y_data_list.append(tmp_ydata[i][0])
    return y_data_list


def GBDT(x_1, x_2, x_3, x_4, y_):
    df = pd.concat([pd.DataFrame(x_1, columns=['gslx']), pd.DataFrame(x_2, columns=['gzlx']),
                    pd.DataFrame(x_3, columns=['gzdz']), pd.DataFrame(x_4, columns=['xl']),
                    pd.DataFrame(y_, columns=['gz'])], axis=1)
    x_all = df.drop(columns='gz')
    gz = df['gz']
    x_all_train, x_all_test, gz_train, gz_test = train_test_split(x_all, gz, test_size=0.2, random_state=123)  # 划分测试集
    model = GradientBoostingRegressor(random_state=123, min_weight_fraction_leaf=0.2)  # 搭建 GBDT 回归模型
    model.fit(x_all_train, gz_train)  # 训练模型
    # 模型评估
    gz_pred = model.predict(x_all_test)
    a = pd.DataFrame()
    a['预测值'] = list(gz_pred)
    a['实际值'] = list(gz_test)
    print(a)

    # 预测效果
    score = model.score(x_all_test, gz_test)
    print(score)

    # 变量相关性
    print(model.feature_importances_)


if __name__ == '__main__':
    # insert_table()  # 只执行一次，请勿多次执行插值
    x1 = get_dummies_job("gslx")
    x2 = get_dummies_job("gzlx")
    x3 = get_dummies_job("gzdz")
    x4 = get_dummies_job("xl")
    y = y_data()
    GBDT(x1, x2, x3, x4, y)
    # dataPre()  # gzdz-xl分词插值，执行一次即可，多次执行浪费性能
