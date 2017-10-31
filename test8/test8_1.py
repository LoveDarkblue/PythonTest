# def readfile(filepath):
#     return open(filepath, 'r')
#
#
# t = None
# try:
#     t = readfile('test8_1.py')
#
#     print(t.read())
# finally:
#     if t:
#         t.close()
#         print('close')

with open('test8_1.py', 'r') as f:
    for l in f.readlines():
        print(l.strip())


f = open('test.jpg', 'rb')