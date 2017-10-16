class Person(object):
    __slots__ = ('name', 'sex')


class Student(Person):
    pass
    # __slots__ = ('addr', 'id')


s = Student()
s.name = 'mary'
s.id = 123
print(s.name, s.id)
