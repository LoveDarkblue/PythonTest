from functools import reduce


# reduce结合map实现str转Int
def str2int(s):
    def f4(x, y):
        return x * 10 + y

    def f5(s1):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[s1]

    return reduce(f4, map(f5, s))


print(str2int("123456"))
