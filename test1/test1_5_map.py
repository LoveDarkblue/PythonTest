# 定义一个dict
students = {'z1': 18,
            'z2': 19,
            "z3": 20,
            'z3': 21, }
# 另一种定义的方式
# students = dict([('z1', 18), ('z2', 19)])

# 取值
print(students['z1'], students.get('z2'))

# 获取一个不存在的键对应的值
print(students.get('zz'))

# 获取一个键对应的值，如果不存在赋默认值
print(students.get('zz', 123))

# 判断z1是否在students中
print('z1' in students)

# 删除一对键值
print(students.pop("z1"))
print(students)

# 定义一个set
s = set([1, 1, 2, 2, 3])
# s = {1, 1, 2, 2, 3}
print(s)

# 删除元素
s.remove(1)
# 增加元素
s.add(4)
print(s)

s1 = {3, 4, 5}
# 取s和s1的交集
print(s & s1)
# 取s和s1的并集
print(s | s1)
