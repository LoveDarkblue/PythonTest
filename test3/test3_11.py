# 偏函数
import functools


def f1(x, y=2):
    print(x, y)


f1(1)
f1(1, 3)

f2 = functools.partial(f1, y=6)

f2(1)
f2(6)

# 默认十进制
print(int('123'))
# 按16进制输出
print(int('123', base=16))

int16 = functools.partial(int, base=16)
print(int16('123'))
