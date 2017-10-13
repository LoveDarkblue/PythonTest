class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def f1(self, msg):
        print('persion say ' + msg)


p = Person("Tom", 19)
print(hasattr(p, "name"))

setattr(p, "name", 'Mary')
print(getattr(p, 'name', "11"))  # 第三个参数是默认值，如果获取不到就返回这个默认值

print(getattr(p, "sex", "男"))

f = getattr(p, 'f1')
f('sss')
