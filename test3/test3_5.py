# 筛选出一个序列中所有能整除2的数
def f1(i):
    return i % 2 == 0


l = filter(f1, [1, 2, 3, 4, 5])
print(list(l))
