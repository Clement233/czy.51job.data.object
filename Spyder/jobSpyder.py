import os
import random
import time

import requests

import jobPymysql


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


# 定义 json 文件网页爬取函数
def getdata(job_url: str):
    param = {
        "lang": "c",
        "postchannel": "0000",
        "workyear": "01",
        "cotype": "99",
        "degreefrom": "99",
        "jobterm": "99",
        "companysize": "99",
        "ord_field": "0",
        "dibiaoid": "0",
        "line": "",
        "welfare": "",
    }
    co = open('cookie.txt')
    cookies = co.read()
    co.close()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": 'gzip, deflate, br',
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "{}".format(cookies),
        "DNT": "1",
        "Host": "search.51job.com",
        "Referer": "https://search.51job.com/list/030000,000000,0000,00,9,99,+,2,"
                   "1.html?lang=c&postchannel=0000&workyear=01&cotype=99&degreefrom=99&jobterm=99&companysize=99"
                   "&ord_field=0&dibiaoid=0&line=&welfare=",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"'
    }
    s = requests.Session()
    # noinspection PyBroadException
    proxy = get_proxy().get("proxy")
    response = s.get(url=job_url, params=param, headers=headers, proxies={"http": "http://{}".format(proxy)})
    engine_jds_data = response.json()["engine_jds"]
    # 删除代理池中代理
    delete_proxy(proxy)
    return engine_jds_data


if __name__ == '__main__':
    # 断点续传
    f = open('cache.txt')
    if not os.path.getsize('cache.txt'):
        with open("cache.txt", 'w') as cache:
            cache.write("{}".format(1))
    c = f.read()
    f.close()
    i = int(c)
    outputdata = []
    try:
        while i < 1000:
            sleeptime = random.randint(3, 6)
            time.sleep(sleeptime)
            url = "https://search.51job.com/list/030000,000000,0000,00,9,99,+,2,{0}.html".format(i)
            url_data = getdata(job_url=url)
            # 数据提取
            for u in range(len(url_data)):
                data = [int(url_data[u]['jobid']),
                        int(url_data[u]['coid']),
                        url_data[u]['job_href'],
                        url_data[u]['job_name'],
                        url_data[u]['company_href'],
                        url_data[u]['company_name'],
                        url_data[u]['providesalary_text'],
                        url_data[u]['workarea_text'],
                        url_data[u]['companytype_text'],
                        url_data[u]['issuedate'],
                        url_data[u]['jobwelf'],
                        ",".join(url_data[u]['attribute_text']),  # 列表转字符串
                        url_data[u]['companysize_text'],
                        url_data[u]['companyind_text']]
                outputdata.append(data)
            L = len(url_data)
            # 数据库存储
            for q in range(0, 50):
                sql_insert = "insert into jobTable " \
                             "(jobid, coid, job_href, job_name, company_href, company_name, providesalary_text, " \
                             "workarea_text, companytype_text, issuedate, jobwelf, attribute_text, companysize_text, " \
                             "companyind_text) " \
                             "values(" \
                             "%d, %d, '%s', '%s', '%s', " \
                             "'%s', '%s', '%s', '%s', '%s', " \
                             "'%s', '%s', '%s', '%s') "
                values = tuple(outputdata[q])
                if not jobPymysql.cursor.execute(
                        "select * from jobTable where jobid={}".format(outputdata[q][0])):
                    jobPymysql.cursor.execute(sql_insert % values)
                    jobPymysql.conn.commit()
                    print(values)
                else:
                    print("重复值，跳过,目前是第{}页".format(i))
            print("----------------------------------------")
            outputdata = []
            i += 1
    except KeyError as KError:
        print(KError)
        pass
    except Exception as error:
        with open("cache.txt", 'w') as cache:
            cache.write("{}".format(i))
            cache.close()
            print('已进行断点续传缓存！')
        print(f"程序错误:{error}或已过期，目前是第{i}页。")
        inputcookie = input("请尝试输入新的 cookie：")
        with open("cookie.txt", 'w') as cookie:
            cookie.write("{}".format(inputcookie))
            cookie.close()
        os.system('python jobSpyder.py')
    except KeyboardInterrupt as kbi:
        # 断点续传缓存
        with open("cache.txt", 'w') as cache:
            cache.write("{}".format(i))
            cache.close()
            print('已进行断点续传缓存！')
