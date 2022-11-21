from Spyder import jobPymysql


def mysqltypeconversion():
    sql_providesalary_text = 'ALTER TABLE jobTable MODIFY COLUMN providesalary_text float'
    jobPymysql.cursor.execute(sql_providesalary_text)
    jobPymysql.conn.commit()
    sql_companysize_text = 'ALTER TABLE jobTable MODIFY COLUMN companysize_text int'
    jobPymysql.cursor.execute(sql_companysize_text)
    jobPymysql.conn.commit()
