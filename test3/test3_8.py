def f1():
    count = []
    for i in range(3):
        def f2():
            return i * i

        count.append(f2)
    return count


m = f1()
print(m[0](), m[1](), m[2]())


def f3():
    count = []

    def f4(j):
        def f5():
            return j * j

        return f5

    for i in range(3):
        # 带括号的方法会立即执行，所以用的是i的当前值
        count.append(f4(i))
    return count


m1 = f3()
print(m1[0](), m1[1](), m1[2]())
