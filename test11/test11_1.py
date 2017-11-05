import re

s1 = 'abc\-123456'
m1 = r'^[a-z]{3}\-\d{3,6}$'
print(s1)
print(m1)
match = re.match(m1, s1)
print(match)

s = r'ABC\\-001'
print(s)