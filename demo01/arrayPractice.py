# _*_ coding = utf-8 _*_    设置文件中文编码
# @Time : 2022/2/14
# @Author King
# @File : arrayPractice.py        当前文件名
# @Software  当前编译器


# 数组练习
nums = [1, 4, 6, 8, 11]
target = 10;
res = []


# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return i, j
#
#
# res = list(twoSum(nums, target))
# print(res)


def twoSum(nums, target):
    dict1 = {}
    n = len(nums)
    for i in range(n):
        if target - nums[i] in dict1.keys():
            return i, dict1.get(target - nums[i])
        dict1[nums[i]] = i
    return []


res = list(twoSum(nums, target))
print(res)
