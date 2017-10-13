# 装饰器
import functools


def d(func):
    def wrapper(*args, **kwargs):  # 一个可变参数加一个关键字参数可接收任意参数的调用
        print('before call %s():' % func.__name__)  # .__name__为获取该函数的name的方法
        func1 = func(*args, **kwargs)
        print('after call %s():' % func.__name__)
        return func1

    return wrapper


@d
def f1():
    print("f1 print")


f1()

def d1(msg):
    def d(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('before call %s():' % func.__name__, msg)
            func1 = func(*args, **kwargs)
            print('after call %s():' % func.__name__, msg)
            return func1

        return wrapper

    return d


@d1('ssssss')
def f2():
    print("f2 print")


f2()
print(f2.__name__)