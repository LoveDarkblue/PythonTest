# 创建一个generator
g = (x * x for x in range(4))
# 获取generator生成的列表里的值
print(next(g), next(g))
# 通过迭代取值
for x in g:
    print(x)

print("----------------------------")

# 输出斐波拉契数列，每个数都是前两个数的和
def methed(index):
    i, j, k = 0, 0, 1
    while i < index:
        print(k)
        j, k = k, j + k
        i = i + 1


methed(10)
