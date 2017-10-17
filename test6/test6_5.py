class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Person (name:%s)" % self.name


p = Person('Tom')
print(p)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    # def __getitem__(self, item):
    #     a, b = 1, 1
    #     for n in range(item):
    #         a, b = b, a + b
    #     return a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for n in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            end = item.stop
            if start is None:
                start = 0
            l = []
            a, b = 1, 1
            for n in range(end):
                if n >= start:
                    l.append(a)
                a, b = b, a + b
            return l


# f = Fib()
# for i in Fib():
#     print(i)
#
# print(f[0:3])


class Student(object):
    def __init__(self):
        self.name = 'Tom'

    def f1(self):
        return lambda: 1 + 1

    def __getattr__(self, item):
        if item == 'age':
            return 20
        if item == 'addr':
            return self.f1()
        if item == 'name':
            return "sss"
        raise AttributeError('Student object has no attribute \'%s\'' % item)


s = Student()
print(s.name)  # 如果已经定义了name,就不会到__getattr__()里找了
print(s.age)
print(s.addr())  # 返回一个可执行的方法，例如返回一个str会报异常


# print(s.a)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


print(Chain('www.baidu.com').login.user)  # 拼接一个接口url


class Obj(object):
    def __call__(self, *args, **kwargs):
        print('sss')


o = Obj()
o()

print(callable(o))
print(callable(Student()))
