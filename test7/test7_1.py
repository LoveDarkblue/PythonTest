def f():
    r = 10 / 0
    print('result:', r)


def f1():
    try:
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')


f()
