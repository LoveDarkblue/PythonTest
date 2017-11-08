import re

s1 = 'abc-123456'
m1 = r'^[a-z]{3}-\d{3,6}$'
match = re.match(m1, s1)
print(match)
if match:
    print('yes')
else:
    print('no')

s2 = 'a,;   b;  c  d'
split = re.split(r'[\s\,\;]+', s2)
print(split)

s1 = 'abc-123456'
m1 = r'^([a-z]{3})-(\d{3,6})$'
match = re.match(m1, s1)
print(match.group(0))
print(match.group(1))
print(match.group(2))

s3 = '12300'
re_match = re.match(r'(\d+)(0*)', s3)  # 贪婪匹配
print(re_match.groups())

s3 = '12300'
re_match = re.match(r'^(\d+?)(0*)$', s3)  # 非贪婪匹配
print(re_match.groups())

re_compile = re.compile(r'^(\w+)@(\w+)(\.[a-zA-Z]+)+$')
print(re_compile.match('Aislli@163.com').groups())
print(re_compile.match('12345@qq.com').groups())
