import itertools

count = itertools.count(10, 2)  # 从10开始，步长2
for i in count:
    print(i)
    if i >= 20:
        break

count1 = itertools.count(10, 2)
takewhile = itertools.takewhile(lambda x: x <= 20, count1)
print(list(takewhile))

cycle = itertools.cycle("123")
n = 0
for i in cycle:
    n = n + 1
    print(i)
    if n > 5:
        break

repeat = itertools.repeat('TEST', 3)  # 输出TEST,共输出3次
for i in repeat:
    print(i)

chain = itertools.chain('ABC', 'DEF')
for i in chain:
    print(i)

groupby = itertools.groupby('AAABBC')
for key, group in groupby:
    print(key, list(group))

groupby = itertools.groupby('AAaBBC', lambda c: c.upper())
for key, group in groupby:
    print(key, list(group))
