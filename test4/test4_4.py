def _f1():
    print('f1')


def _f2():
    print('f2')


def f3(name):
    if name == 'f1':
        return _f1()
    else:
        return _f2()

