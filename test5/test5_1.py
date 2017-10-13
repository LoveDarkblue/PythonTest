class Student(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def printInfo(self):
        print(self.name, self.sex)


std1 = Student("Mary", '女')
std2 = Student('Tom', '男')

std1.printInfo()
std2.printInfo()

std1.age = 18
print(std1.age)
print(std2.age)