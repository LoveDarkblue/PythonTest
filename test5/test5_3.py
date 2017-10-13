class Animal(object):
    def run(self):
        print('Animal is running')


class Cat(Animal):
    pass


class Dog(Animal):
    def run(self):
        print('Dog is running')


def f1(animal):
    animal.run()


f1(Cat())
f1(Dog())
f1(Animal())


class aaa(object):
    def run(self):
        print('aaa is running')


f1(aaa())
