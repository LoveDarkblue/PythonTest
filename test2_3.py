# 生成1到10的list
print(list(range(1, 11)))

# 通过普通for循环生成1*1，2*2...10*10的list
l = []
for i in range(1, 11):
    l.append(i * i)
print(l)

# 通过python生成式生成1*1，2*2...10*10的list
print([i * i for i in range(1, 11)])

# 生成式里加入条件判断
print([i * i for i in range(1, 11) if i % 2 == 0])

# for循环里套for循环
print([i + j for i in "ABC" for j in "123"])

import os

# 列出当前目录下的文件名
print([f for f in os.listdir('.')])

# 将一个list里的字母全部变小写
L = ['A', 'B', 'C', 1, 'D']
print([s.lower() for s in L if isinstance(s, str)])
