def f1(index):
    count = 0
    for i in range(index):
        count = count + i
    return count


print(f1(5))


def f2(index):
    def f3():
        count = 0
        for i in range(index):
            count = count + i
        return count

    return f3

f = f2(5)
print(f2(5))
print(f)
print(f())
