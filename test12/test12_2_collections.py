from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# deque
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)

# defaultdict
defaultd = defaultdict(lambda: "sss")
defaultd['key1'] = 'abc'
print(defaultd['key1'])
print(defaultd['key2'])

# OrderedDict
d1 = dict([('x', 1), ('y', 2), ('z', 3)])  # 无序
print(d1)

d2 = OrderedDict([('x', 1), ('y', 2), ('z', 3)])  # 有序
for i in d2:
    print('%s=%s' % (i, d2[i]))

# Counter
c = Counter()
for i in 'aaabcccdd':
    c[i] = c[i] + 1
print(c)
