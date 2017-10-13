# 定义一个函数
def sum(i1, i2):
    return i1 + i2


print(sum(1, 2))


# 定义一个函数，并定义一个有默认值的变量
def method1(name, age, addr='shanghai'):
    print('name:' + name)
    print('age:' + age)
    print('addr:' + addr)


method1('大一', '19', 'beijing')
method1('大二', '20')


# 定义一个默认为空list的变量
def method2(l=[]):
    l.append('111')
    return l


print(method2())  # L初始为[]，运行后被赋值为['111']
print(method2())  # L刚被赋值后初始为['111']，运行后被赋值为['111','111']
print(method2())


# 解决上面的错误
def method3(l=None):
    if l is None:
        l = []
    l.append('111')
    return l


print(method3())
print(method3())
print(method3())


def method4(*i):
    s = 0
    for n in i:
        s += n
    return s


print(method4(1, 2, 3))

# 把一个list作为参数传入
l1 = [1, 2, 3]
print(method4(*l1))


def method5(name, age, **i):
    print('''
name:%s
age:%s
i:%s
    ''' % (name, age, i))


method5('AA', '20', arg1='11', arg2='22')

# 把一个dict作为参数传入
d1 = {'arg1': 11, 'arg2': 22}
method5('BB', '20', **d1)


def method6(name, age, *, arg1, arg2):
    print(name, age, arg1, arg2)


# 命名关键字参数必需传入参数名，否则报错
# method6('CC', 20, 1, 2) #错误的写法
method6('CC', 20, arg1=1, arg2=2)


# 如果参数中有一个可变参数了，后面的命名关键字参数就不需要再写*隔开了
def method7(name, age, *arg1, arg2):
    print(name, age, arg1, arg2)


method7("DD", 20, [1, 2], arg2=2)


def method8(arg1, arg2=2, *arg3, arg4, **arg5):
    print('''
    arg1:%s
    arg2:%s
    arg3:%s
    arg4:%s
    arg5:%s
    ''' % (arg1, arg2, arg3, arg4, arg5))


method8("111", arg4=4)
method8("111", 22, arg4=4)
method8("111", 22, '3a', '3b', arg4=4)
method8("111", 22, "3a", "3b", arg4=4, arg5=555)
