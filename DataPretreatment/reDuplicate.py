from Spyder import jobPymysql

sql_reDuplicate = 'DELETE FROM jobTable WHERE id in ( SELECT b.id  FROM  (  SELECT t.* FROM jobTable  t, ' \
                  '(SELECT job_name, COUNT(job_name), company_name, COUNT(company_name) FROM jobTable GROUP BY ' \
                  'job_name, company_name HAVING  (COUNT(job_name) > 1) AND  (COUNT(company_name) > 1) ) a WHERE ' \
                  't.job_name=a.job_name AND t.company_name=a.company_name ) b   WHERE b.id NOT IN ( SELECT min(id) ' \
                  'as id FROM ( SELECT t.* FROM  jobTable t, ( SELECT job_name, COUNT(job_name), company_name, ' \
                  'COUNT(company_name) FROM jobTable GROUP BY job_name, company_name HAVING  (COUNT(job_name) > 1) ' \
                  'AND  (COUNT(company_name) > 1) ) a WHERE t.job_name=a.job_name AND t.company_name=a.company_name ' \
                  ')a  GROUP BY a.job_name,a.company_name ) ) '
jobPymysql.cursor.execute(sql_reDuplicate)
jobPymysql.conn.commit()
print("已完成去重")
