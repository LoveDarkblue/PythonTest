# 普通大小排序
l = [2, 5, 1, -3, 6]
print(sorted(l))

# 转换成正数后再排序
print(sorted(l, key=abs))

# 英文排序，按首字母的ascll码的大小排序
l1 = ["Ckl", "Gak", "adfj", "bafk"]
print(sorted(l1))

# 转换成小写后再排序
print(sorted(l1, key=str.lower))

print(sorted(l1, key=str.lower, reverse=True))
