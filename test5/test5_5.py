import types
import test5.test5_3

print(type(123))
print(type('123'))
print(type(123) == int)
print(type('abc') == str)
print(type('abc') == type('1'))


# 判断是否是函数
def f1():
    pass


print(type(f1) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(type(test5.test5_3.Cat()) == test5.test5_3.Animal)  # false

print(isinstance(test5.test5_3.Cat(), test5.test5_3.Animal))

print(isinstance((1, 2, 3), (int, str)))

# 获取'123'这个实例里所有的属性和方法
print(dir('123'))

class ddd(object):
    def __len__(self):
        return 100

d = ddd()
print(len(d))
