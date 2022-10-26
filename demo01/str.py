# _*_ coding = utf-8 _*_    设置文件中文编码
# @Time : 2022/2/13
# @Author King
# @File : str.py        当前文件名
# @Software  当前编译器
#  字符串处理

s = "  wfew:  lisi  \n"

content = s.rstrip().lstrip().split(":")
print(content)
# res = s.split()
#
# print(res)
# res = res[0::2]
#
# dict1 = dict([res])
# print(res)
# print("dict1 : ", dict1)
#
# dict1.update({"name":"zhang3"})
# print("dict1 : ", dict1)