def func1(n):
    if n == 1:
        return 1
    return n + func1(n - 1)

print(func1(100))
