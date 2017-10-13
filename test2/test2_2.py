from collections import Iterable

l = [1, 2, 3]

d = {"A": 1, "B": 2, "C": 3}

# 遍历list
for i in l:
    print(i)

# 遍历dict的key
for j in d:
    print(j)
# 遍历dict的value
for j in d.values():
    print(j)

# 遍历dict的key和value
for j in d:
    print(j, d[j])
# 遍历dict的key和value
for i, j in d.items():
    print(i, j)

# 遍历字符串
s = "ABC"
for i in s:
    print(i)

print(isinstance(s, Iterable))
print(isinstance(123, Iterable))


l = [1, 2, 3]
for i, j in enumerate(l):
    print(i, j)
