from io import StringIO, BytesIO

f = StringIO()
f.write('hi')
f.write(' ')
f.write('python')
print(f.getvalue())

f = StringIO('a!\nb!\nc!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f1 = BytesIO()
f1.write('中国'.encode('UTF-8'))
print(f1.getvalue())
