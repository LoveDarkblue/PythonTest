# 匿名函数
def f1(x):
    return x + x


print(list(map(f1, [1, 2, 3])))

print(list(map(lambda x: x + x, [1, 2, 3])))

f2 = lambda x: x + x
print(f2(6))
