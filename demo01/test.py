# _*_ coding = utf-8 _*_    设置文件中文编码
# @Time : 2022/8/18
# @Author King
# @File : test.py        当前文件名
# @Software  当前编译器

nums = [1, 3, 4, 5]
max_ = sum(nums)
dp = []


def get_w(sub):
    # 按照二进制加法计算，并且不计算走位， 计算重量
    t = 0
    for n in set(nums).difference(sub):
        # 按照二进制加法计算
        t = t ^ n
    return t


def dfs(w, sub):
    # w 是已经分过得(A)，按照二进制加法计算的重量
    # sub 是未分配的苹果 (B)
    if w == get_w(sub):
        tot = sum(sub)
        # 取最大实际重量 保存在 dp
        dp.append(max(tot, max_ - tot))
        return
    elif len(sub) == len(nums) - 1:
        # 不能把苹果全部分给 某一堆
        return
    else:
        # 生成可能的 堆组合，计算进行重量比较
        for wi in nums:
            if wi not in sub:
                dfs(w ^ wi, sub.union({wi}))


for w in nums:
    dfs(w, {w})

if dp:
    print(max(dp))
else:
    print(-1)
