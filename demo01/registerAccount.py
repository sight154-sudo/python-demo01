# _*_ coding = utf-8 _*_    设置文件中文编码
# @Time : 2022/10/25
# @Author King
# @File : registerAccount.py.py        当前文件名
# @Software  当前编译器

'''
 设置模板文件头
# _*_ coding = utf-8 _*_    设置文件中文编码
# @Time : ${DATE}
# @Author King
# @File : ${NAME}.py        当前文件名
# @Software ${PROCUDT_NAME} 当前编译器
'''

import requests
import logging


# url = "https://www.baidu.com"
#
# response = requests.post(url)
# response.encoding = "UTF-8"
# print(response.text)


def login():
    url = "http://localhost:8080/login"

    data = {"username": "张三", "password": "123"}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'
    }

    response = requests.post(url, json=data, headers=headers)
    cookies = response.cookies
    print("cookie" + str(cookies))
    cookie_t = requests.utils.dict_from_cookiejar(cookies)
    print(cookie_t)
    cookie_str = ""
    for cookie in cookie_t:
        cookie_str += cookie + "=" + cookies[cookie] + ";"
    f = open("cookie.txt", "w+", encoding="utf-8")
    f.writelines(cookie_str)


def queryApi(cookie):
    url="http://localhost:8080/query"
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
        'Cookie':cookie
    }
    data={
        "apiName":"jjsldjlb"
    }
    r = requests.get(url, json=data, headers=header)
    logging.info(r.text)

if __name__ == "__main__":
    login()
    log = logging.getLogger()
    log.setLevel("DEBUG")
    f = open("cookie.txt", "r+", encoding="utf-8")
    cookie_str=""
    while True:
        content = f.readline()
        if len(content) == 0:
            logging.info("读取cookie完毕")
            break
        cookie_str+=content
    queryApi(cookie_str)

