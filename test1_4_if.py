a = 85
# if判断语句
if a > 90:
    print("A")
elif a > 80:
    print('B')
else:
    print('C')

t = [1, 2, 3, 4, 5, 6]
s = 0
# for循环
for i in t:
    print(i)
    s += i
print(s)

# range生成0到100的整数序列，再用list转成list后通过sum操作符可计算出整个list的和
print(sum(list(range(101))))

# while操作
t1 = 100
s1 = 0
while t1 > 0:
    s1 += t1
    t1 -= 1
    if t1 % 2 == 0:
        continue
    if t1 < 50:
        break
print(s1)
