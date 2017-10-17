class Person(object):
    def f1(self):
        print('f1')


class Person1(object):
    def f2(self):
        print('f2')


class Person2(Person, Person1):
    pass


p = Person2()
p.f1()
p.f2()
