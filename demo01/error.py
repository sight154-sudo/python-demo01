# _*_ coding = utf-8 _*_    设置文件中文编码
# @Time : 2022/2/14
# @Author King
# @File : error.py        当前文件名
# @Software  当前编译器


#  异常的使用
'''
try:
    f = open("123.txt", "r")

except IOError as e:
    print(e)
'''
'''
def testError():
    try:
        print("---test-------1---")
        f = open("str.py","r")
        print("---test-------2---")
        print(num)
    except (NameError,IOError) as e:
        print(e)

testError()
'''

f = open("test.txt", "w+", encoding="utf-8")
f.seek(0, 0)
f.writelines("  静夜思  \n")
f.writelines("床前明月光\n")
f.writelines("疑是地上霜\n")
f.writelines("举头望明月\n")
f.writelines("低头思故乡\n")
f.close()


# f.close()

# def readGushi(f):
#     try:
#         try:
#             target = open("copy.txt", "w", encoding="utf-8")
#             f.seek(0, 0)
#             while True:
#                 content = f.readline()
#                 if len(content) == 0:
#                     print("文件复制完毕")
#                     break
#                 target.writelines(content)
#         finally:
#             target.close()
#             f.close()
#     except Exception as e:
#         print(e)
#
#
# readGushi(f)


def readFile(f, w):
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                print("copy end...")
                break
            writeFile(w, content)
    except Exception as ee:
        print("copy error", ee)
    finally:
        f.close()
        w.close()

def writeFile(w, content):
    try:
        w.writelines(content)
    except IOError as e:
        print("copy write error", e)


f = open("test.txt", "r", encoding="utf-8")
w = open("copy.txt", "w", encoding="utf-8")
readFile(f, w)
# def readGushi():
#     try:
#         source = open("test.txt", "r", encoding="utf-8")
#         target = open("copy.txt", "w", encoding="utf-8")
#         try:
#             while True:
#                 content = source.readline()
#                 if len(content) == 0:
#                     print("文件复制完毕")
#                     break
#                 target.writelines(content)
#         finally:
#             source.close()
#             target.close()
#     except Exception as rs:
#         print("文件复制失败!!!", rs)
#
#
# readGushi()
