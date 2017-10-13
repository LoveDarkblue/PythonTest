class Student(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.__age = 18

    def printInfo(self):
        print(self.name, self.sex)

    def get_age(self):
        return self.__age


std1 = Student("Mary", '女')

std1.printInfo()

print(std1.get_age())

std1.__age = 20
print(std1.__age)
print(std1.get_age())
