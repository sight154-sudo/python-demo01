# _*_ coding = utf-8 _*_    设置文件中文编码
# @Time : 2022/2/12
# @Author King
# @File : hello.py        当前文件名
# @Software  当前编译器


# def testfun():
#     print("hello world")
#
#
# testfun()

'''
f = open("test.txt", 'w')

f.write("hello world\n")


f.close()
'''
import os

# f = open("test.txt", "r+", encoding="utf-8")


# f.seek(2, 0)
#
# tmp = f.tell()
# print(tmp)
# print(type(tmp))
# content = f.read(5)
# print(content)
# content = f.read(5)
# print(content)
# content = f.read(1)
# print(content)
# content = f.read(1)
# print(content)
# content = f.read(1)
# print(content)

# content = f.readlines()
# print(content)
#
# f.close()
#
# s = "你好"
# s = s.encode("gbk");
# print(s)
# s = s.decode("gbk")
# print(s)


# f = open("C:\\Users\\King\\Desktop\\1.txt", "r+")
# w = open("C:\\Users\\King\\Desktop\\2.txt", "w+")
# content = f.readlines()
# w.writelines(content)
# print(content)
# f.close()
# w.close()
r = open("demo.txt", "r+",encoding="utf-8")

dict1 = {}
while (True):
    content = r.readline()
    print("content : %s" % content)
    if (content == ""):
        break
    res = content.lstrip().rstrip().split(":")
    print("res: %s" % res)
    res = res[0::]
    print("res after : %s" % res)
    dict1[res[0].lstrip().rstrip()] = res[1].lstrip().rstrip()
    # dict1.update(tmp)
r.close()
print(dict1)
