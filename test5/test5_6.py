class Person(object):
    name = "Person"

    def __init__(self, name):
        self.name = name


p = Person("Tom")

print(p.name)  # 实例的name属性
print(Person.name)  # 类的name属性
p.name = 'Mary'  # 修改实例的name属性
print(p.name)
print(Person.name)
del p.name  # 删除实例的name
print(p.name)
