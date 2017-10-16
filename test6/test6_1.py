from types import MethodType


class Person(object):
    pass


p = Person()


def sayhello(self, msg):
    print(msg)


Person.name = 'Mary'  # 动态的给类定义一个属性
print(p.name)

Person.sayhello = sayhello # 动态的给类设置一个方法
p.sayhello('hello')

p1 = Person()
print(p1.name)
