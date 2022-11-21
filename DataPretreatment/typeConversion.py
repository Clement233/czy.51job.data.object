import math
import re

from DataPretreatment import mysqlTypeConversion
from Spyder import jobPymysql

sql_idmin = 'select id from jobTable order by id asc limit 1;'
jobPymysql.cursor.execute(sql_idmin)
jobPymysql.conn.commit()
idmin = jobPymysql.cursor.fetchall()[0][0]

sql_idmax = 'select id from jobTable order by id desc limit 1;'
jobPymysql.cursor.execute(sql_idmax)
jobPymysql.conn.commit()
idmax = jobPymysql.cursor.fetchall()[0][0]


def providesalary():
    try:
        for i in range(idmin, idmax + 1):
            sql_select = f'select providesalary_text from jobTable where id={i}'
            jobPymysql.cursor.execute(sql_select)
            jobPymysql.conn.commit()
            job_salary_tuple = jobPymysql.cursor.fetchall()
            if job_salary_tuple:
                job_salary_all = job_salary_tuple[0][0]

                # 匹配*-*千
                salary1 = re.compile(r'\d+-\d+千$|\d+\.\d+-\d+千$|\d+-\d+\.\d+千$|\d+\.\d+-\d+\.\d+千$')
                job_salary1 = salary1.findall(job_salary_all)
                if job_salary1:
                    a = job_salary1[0].replace('千', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = (float(a[1]) * 1000 + float(a[0]) * 1000) / 2
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 1')

                # 匹配*-*万
                salary2 = re.compile(r'\d+-\d+万$|\d+\.\d+-\d+万$|\d+-\d+\.\d+万$|\d+\.\d+-\d+\.\d+万$')
                job_salary2 = salary2.findall(job_salary_all)
                if job_salary2:
                    a = job_salary2[0].replace('万', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = (float(a[1]) * 10000 + float(a[0]) * 10000) / 2
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 2')

                # 匹配*千-*千
                salary3 = re.compile(r'\d+千-\d+千$|\d+\.\d+千-\d+千$|'
                                     r'\d+千-\d+\.\d+千$|\d+\.\d+千-\d+\.\d+千$')
                job_salary3 = salary3.findall(job_salary_all)
                if job_salary3:
                    a = job_salary3[0].replace('千', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = (float(a[1]) * 1000 + float(a[0]) * 1000) / 2
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 3')

                # 匹配*千-*万
                salary4 = re.compile(r'\d+千-\d+万$|\d+\.\d+千-\d+万$|'
                                     r'\d+千-\d+\.\d+万$|\d+\.\d+千-\d+\.\d+万$')
                job_salary4 = salary4.findall(job_salary_all)
                if job_salary4:
                    a = job_salary4[0].replace('千', '') or job_salary4[0].replace('万', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = (float(a[1]) * 10000 + float(a[0]) * 1000) / 2
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 4')

                # 匹配*万-*千
                salary5 = re.compile(r'\d+万-\d+千$|\d+\.\d+万-\d+千$|'
                                     r'\d+万-\d+\.\d+千$|\d+\.\d+万-\d+\.\d+千$')
                job_salary5 = salary5.findall(job_salary_all)
                if job_salary5:
                    a = job_salary4[0].replace('千', '') or job_salary4[0].replace('万', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = (float(a[1]) * 1000 + float(a[0]) * 10000) / 2
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 5')

                # 匹配*万-*万
                salary6 = re.compile(r'\d+万-\d+万$|\d+\.\d+万-\d+万$|'
                                     r'\d+万-\d+\.\d+万$|\d+\.\d+万-\d+\.\d+万$')
                job_salary6 = salary6.findall(job_salary_all)
                if job_salary6:
                    a = job_salary6[0].replace('万', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = (float(a[1]) * 10000 + float(a[0]) * 10000) / 2
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 6')

                # 匹配*-*千/年
                salary7 = re.compile(r'\d+-\d+千/年$|\d+\.\d+-\d+千/年$|\d+-\d+\.\d+千/年$|\d+\.\d+-\d+\.\d+千/年$')
                job_salary7 = salary7.findall(job_salary_all)
                if job_salary7:
                    a = job_salary7[0].replace('千/年', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = ((float(a[1]) * 1000 + float(a[0]) * 1000) / 2) / 12
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 7')

                # 匹配*-*万/年
                salary8 = re.compile(r'\d+-\d+万/年$|\d+\.\d+-\d+万/年$|\d+-\d+\.\d+万/年$|\d+\.\d+-\d+\.\d+万/年$')
                job_salary8 = salary8.findall(job_salary_all)
                if job_salary8:
                    a = job_salary8[0].replace('万/年', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = ((float(a[1]) * 10000 + float(a[0]) * 10000) / 2) / 12
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 8')

                # 匹配*-*千·13薪
                salary9 = re.compile(r'\d+-\d+千·13薪$|\d+\.\d+-\d+千·13薪$|\d+-\d+\.\d+千·13薪$|\d+\.\d+-\d+\.\d+千·13薪$')
                job_salary9 = salary9.findall(job_salary_all)
                if job_salary9:
                    a = job_salary9[0].replace('千·13薪', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = ((float(a[1]) * 1000 + float(a[0]) * 1000) / 2) * 13 / 12
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 9')

                # 匹配*-*万·13薪
                salary10 = re.compile(r'\d+-\d+万·13薪$|\d+\.\d+-\d+万·13薪$|\d+-\d+\.\d+万·13薪$|\d+\.\d+-\d+\.\d+万·13薪$')
                job_salary10 = salary10.findall(job_salary_all)
                if job_salary10:
                    a = job_salary10[0].replace('万·13薪', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = ((float(a[1]) * 10000 + float(a[0]) * 10000) / 2) * 13 / 12
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 10')

                # 匹配*千-*万·13薪
                salary11 = re.compile(
                    r'\d+千-\d+万·13薪$|\d+\.\d+千-\d+万·13薪$|\d+千-\d+\.\d+万·13薪$|\d+\.\d+千-\d+\.\d+万·13薪$')
                job_salary11 = salary11.findall(job_salary_all)
                if job_salary11:
                    a = job_salary11[0].replace('千', '') or job_salary11[0].replace('万·13薪', '')
                    a = re.findall(r'\d+\.\d+|\d+', a)
                    a = ((float(a[1]) * 10000 + float(a[0]) * 1000) / 2) * 13 / 12
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 11')

                # 匹配*元/天
                salary12 = re.compile(r'\d+元/天$')
                job_salary12 = salary12.findall(job_salary_all)
                if job_salary12:
                    a = job_salary12[0].replace('元/天', '')
                    a = float(a) * 30.5
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 12')

                # 匹配*千及以下
                salary13 = re.compile(r'\d+千及以下$')
                job_salary13 = salary13.findall(job_salary_all)
                if job_salary13:
                    a = job_salary13[0].replace('千及以下', '')
                    a = float(a) * 1000
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 13')

                # 匹配*万及以下
                salary14 = re.compile(r'\d+万及以下$')
                job_salary14 = salary14.findall(job_salary_all)
                if job_salary14:
                    a = job_salary14[0].replace('万及以下', '')
                    a = float(a) * 10000
                    sql_update = 'update jobTable set providesalary_text={} where id={}'.format(a, i)
                    jobPymysql.cursor.execute(sql_update)
                    jobPymysql.conn.commit()
                    print(a, '，类型 14')

            else:
                sql_del = f'DELETE FROM jobTable WHERE id={i}'
                jobPymysql.cursor.execute(sql_del)
                jobPymysql.conn.commit()
    except TypeError:
        print('你或许已经完成providesalary_text字段转换，请自行查看此字段是否已转换为 float')


def companysize():
    try:
        for x in range(2):
            for i in range(idmin, idmax + 1):
                sql_select = f'select companysize_text from jobTable where id={i}'
                jobPymysql.cursor.execute(sql_select)
                jobPymysql.conn.commit()
                job_companysize_tuple = jobPymysql.cursor.fetchall()
                if job_companysize_tuple:
                    job_companysize_all = job_companysize_tuple[0][0]
                    # 匹配*-*人
                    companysize1 = re.compile(r'\d+-\d+人$')
                    job_companysize1 = companysize1.findall(job_companysize_all)
                    if job_companysize1:
                        a = job_companysize1[0].replace('人', '')
                        a = re.findall(r'\d+', a)
                        a = (int(a[1]) + int(a[0])) / 2
                        a = float(a)
                        a = math.floor(a)
                        sql_update = 'update jobTable set companysize_text={} where id={}'.format(a, i)
                        jobPymysql.cursor.execute(sql_update)
                        jobPymysql.conn.commit()
                        print(a, '，类型 1')

                    # 匹配*-*人以上
                    companysize2 = re.compile(r'\d+人以上$')
                    job_companysize2 = companysize2.findall(job_companysize_all)
                    if job_companysize2:
                        a = job_companysize2[0].replace('人以上', '')
                        a = re.findall(r'\d+', a)
                        a = int(a[0])
                        a = float(a)
                        a = math.floor(a)
                        sql_update = 'update jobTable set companysize_text={} where id={}'.format(a, i)
                        jobPymysql.cursor.execute(sql_update)
                        jobPymysql.conn.commit()
                        print(a, '，类型 2')

                    # 匹配少于*人
                    companysize3 = re.compile(r'少于\d+人$')
                    job_companysize3 = companysize3.findall(job_companysize_all)
                    if job_companysize3:
                        a = job_companysize3[0].replace('少于', '') and job_companysize3[0].replace('人', '')
                        a = re.findall(r'\d+', a)
                        a = int(a[0])
                        a = float(a)
                        a = math.floor(a)
                        sql_update = 'update jobTable set companysize_text={} where id={}'.format(a, i)
                        jobPymysql.cursor.execute(sql_update)
                        jobPymysql.conn.commit()
                        print(a, '，类型 3')
    except TypeError:
        print('你或许已经完成companysize_text字段转换，请自行查看此字段是否已转换为 int')


def delnotcompliance():
    for i in range(idmin, idmax):
        sql_select = f'select providesalary_text from jobTable where id={i}'
        jobPymysql.cursor.execute(sql_select)
        jobPymysql.conn.commit()
        job_providesalary_tuple = jobPymysql.cursor.fetchall()
        if job_providesalary_tuple:
            job_providesalary_all = job_providesalary_tuple[0][0]
            try:
                float(job_providesalary_all)
            except Exception as error:
                sql_del = f'DELETE FROM jobTable WHERE id={i}'
                jobPymysql.cursor.execute(sql_del)
                jobPymysql.conn.commit()
                print(error, 'id 为', i, '，数据不合规，已进行删除', '值为：', job_providesalary_all)

        sql_select = f'select companysize_text from jobTable where id={i}'
        jobPymysql.cursor.execute(sql_select)
        jobPymysql.conn.commit()
        job_companysize_tuple = jobPymysql.cursor.fetchall()
        if job_companysize_tuple:
            job_companysize_all = job_companysize_tuple[0][0]
            try:
                a = float(job_companysize_all)
                math.floor(a)
            except Exception as error:
                sql_del = f'DELETE FROM jobTable WHERE id={i}'
                jobPymysql.cursor.execute(sql_del)
                jobPymysql.conn.commit()
                print(error, 'id 为', i, '，数据不合规，已进行删除', '值为：', job_companysize_all)


if __name__ == '__main__':
    providesalary()
    companysize()
    delnotcompliance()
    mysqlTypeConversion.mysqltypeconversion()
