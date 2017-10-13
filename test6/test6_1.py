from types import MethodType


class Person(object):
    pass


p = Person()


def sayhello(self, msg):
    print(msg)


p.sayhello = MethodType(sayhello, p)
p.sayhello('hello')
