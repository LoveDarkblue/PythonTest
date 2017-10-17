from enum import Enum, unique

e = Enum('E', ('A', 'B', 'C'))

for name, member in e.__members__.items():
    print(name, ':', member, ',', member.value)

print(e.A.value, e.C.value)  # value是自动赋值给枚举成员的int常量，默认从1开始


@unique
class Week(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sta = 6


print(Week.Mon)
print(Week['Tue'])
print(Week(0))
print(Week['Wed'].value)
