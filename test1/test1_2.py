print('hello python!')
# 打印多个String
print('x', 'yz')
# 打印多行
print('''line1
line2
line3 line4
line5
''')

print(r'hello,"python"')
print(r'''
hello
lis''')

print('中国'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8'))
print(len('中'))

# 占位符
print('hi,%s,you have %d $' % ('lisa', 101010))

# 前面补空格
print('%d' % 1)
print('%2d' % 1)
print('%3d' % 1)

# 保留两位小数
print('%.2f%%' % 3.1111)
