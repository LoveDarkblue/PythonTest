from functools import reduce

f = abs
a = 1
b = -2


# 将函数作为参数传入到另一个函数
def submit(x, y, z):
    return z(x) + z(y)


print(submit(a, b, f))


def f1(x):
    return x * x


# r是一个Iterator
r = map(f1, [1, 2, 3])
print(list(r))


def f2(x, y):
    return x * y


# r是一个Iterator
r = map(f2, [1, 2, 3], [1, 2, 4])
print(list(r))


def f3(x, y):
    return x + y


r1 = reduce(f3, [1, 2, 3, 4, 5])
print(r1)


# str转Int
def str2int(s):
    def f4(x, y):
        return x * 10 + y

    def f5(s1):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[s1]

    return reduce(f4, map(f5, s))

print(str2int("123456"))
