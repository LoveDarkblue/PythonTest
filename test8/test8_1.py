def readfile(filepath):
    return open(filepath, 'r')


try:
    t = readfile('test8_11.py')

    print(t.read())
finally:
    if t:
        t.close()
