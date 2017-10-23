def f():
    r = 10 / 0
    print('result:', r)


def f1():
    try:
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    else:
        print('no error')
    finally:
        print('finally...')
    print('END')


# f1()


def f2():
    try:
        f()
    except Exception as e:
        print('except:', e)


# f2()


# 自定义一个error类型
class VError(ValueError):
    pass


def f3(i):
    if i == 0:
        raise VError('Invalid value:%d' % i)
    return 10 / i


# f3(0)


def f4():
    try:
        r = 10 / 0
        print('result:', r)
    except Exception as e:
        print('f4', e)
        raise VError('000 error!')
    finally:
        print('finally')
    print('end')


def f5():
    try:
        f4()
    except Exception as e:
        print('f5', e)


f5()
