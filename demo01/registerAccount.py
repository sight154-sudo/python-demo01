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

# url = "https://www.baidu.com"
#
# response = requests.post(url)
# response.encoding = "UTF-8"
# print(response.text)

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
cookie_str=""
for cookie in cookie_t:
    cookie_str += cookie + "=" + cookies[cookie] + ";"
print(cookie_str)



