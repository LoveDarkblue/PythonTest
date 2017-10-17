class Person(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise ValueError('name must be string')
        self._name = value

    @property
    def age(self):
        return 20


p = Person()
p.name = 'Mary'

print(p.age, p.name)
p.age = 11
