from functools import reduce


# reduce

def f3(x, y):
    return x + y


r1 = reduce(f3, [1, 2, 3, 4, 5])
print(r1)

