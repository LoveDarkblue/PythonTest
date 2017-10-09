# map
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
