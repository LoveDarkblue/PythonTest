l = [1, 2, 3, 4, 5, 6]
# 取第0到第3个元素
print(l[0:3])
print(l[:3])

# 取倒数第0到第2个元素
print(l[-2:])

l1 = list(range(10))
# 前6个每隔2个取值
print(l1[:6:2])
# 所以的数每隔3个取值
print(l1[::3])
# 原list不变
print(l1[:])

# 字符串的切分
s = "ABCDEFG"
print(s[:3])
print(s[::2])
