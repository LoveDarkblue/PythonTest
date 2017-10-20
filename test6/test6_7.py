def f(self, msg='python'):
    print('hi %s' % msg)


TestObj = type('TestObj', (object,), dict(hi=f))

t = TestObj()
t.hi()
t.hi(msg='sss')


class MyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['sayHi'] = lambda self, value: cls.f1(self, value)
        attrs['adds'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

    def f1(self, value):
        print(value)


class Person(object, metaclass=MyMetaclass):
    pass


p = Person()
p.sayHi('hi python')


class Mylist(list, metaclass=MyMetaclass):
    pass


mlist = Mylist()
mlist.adds("sss")
print(mlist)
mlist.sayHi('hi python')
