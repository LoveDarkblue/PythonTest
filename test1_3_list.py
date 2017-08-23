# 定义一个list
list = ['111', '222', '333']
# 输出list的长度
print(len(list))
# 在后面添加一项
list.append("444")
# 插入到第一项
list.insert(1, '000')
print(list)
# 输出第1个和倒数第一个和倒数第二个
print(list[1], list[-1], list[-2])
# 删除倒数第二个
list.pop(-2)
print(list)

l = ['sss', 11, True, ["111", "222"]]
print(l)
print(l[0], l[2], l[3][1])

# 定义一个tuple
t = (1, 2, 3)
print(t[1])
# 定义一个空的tuple
t = ()
print(t)
# 定义一个只有一个元素的tuple,必须加个逗号，否则和数学运算符里的()冲突，被认为是1
t = (1,)
print(t)
