import re

# 正则的其它使用
content = '''http://www.baidu.com/bg1.jgp
http://www.baidu.com/bg2.png
http://www.baidu.com/bg3.bmp
'''
# 匹配一段文字里的url和图片类型
# findall 0个组
# rem = re.compile(r'http\:\/\/.+?/\w+\.[a-zA-Z0-9]{3}?')
# findall = rem.findall(content)
# print('findall:', findall, type(findall), type(findall[0]))
#
# # finditer 0个组
# finditer = rem.finditer(content)
# for item in finditer:
#     print('finditer:', item, item.group(0))


# #findall 1个组
# rem = re.compile(r'(http\:\/\/.+?)/\w+\.[a-zA-Z0-9]{3}?')
# findall = rem.findall(content)
# print('findall:', findall, type(findall), type(findall[0]))
#
# # finditer 1个组
# finditer = rem.finditer(content)
# print(finditer)
# for item in finditer:
#     print('finditer:', item, item.groups(), item.group(0), item.group(1))

# findall 2个组
rem = re.compile(r'(http\:\/\/.+?)/\w+\.([a-zA-Z0-9]{3})?')
findall = rem.findall(content)
print('findall:', findall, type(findall), type(findall[0]))

# finditer 2个组
finditer = rem.finditer(content)
print(finditer)
for item in finditer:
    print('finditer:', item, item.groups(), item.group(0), item.group(1), item.group(2))
