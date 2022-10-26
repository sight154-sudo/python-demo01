# _*_ coding = utf-8 _*_    设置文件中文编码
# @Time : 2022/10/27
# @Author King
# @File : excel.py.py        当前文件名
# @Software  当前编译器

import pandas as pd
import random
import logging
import datetime


def read():
    # f = open("C:\\Users\\King\\Desktop\\data.xlsx", "r+", encoding="UTF-8")
    filePath = "C:\\Users\\King\\Desktop\\data.xlsx"
    data = pd.read_excel(filePath)
    data1 = data.replace(["批量客户数据"], "批量客户数据aaa")
    # data1.to_excel(filePath, sheet_name="Sheet1", index=False)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    print(today)

def rand():
    log.info(msg=" rand num is %d" % (random.randint(1000000, 9999999)))
    log.info("aaa")
    num = random.randint(1000000, 9999999)
    print("num is %d" % num)


if __name__ == '__main__':
    read()
    log = logging.getLogger()
    log.setLevel("DEBUG")
    rand()
    log.info(msg="bbb")
