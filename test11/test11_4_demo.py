import re

content = '''
asdfadsfsadfsda-sadfsdaf11http://ws.stream.qqmusic.qq.com/C100001jlxUj2UEa33.m4a?fromtag=466646Aaf11http://ws.stream.qqmusic.qq.com/C100001jlxUj2UEa33.m4a?fromtag=466
'''
rex = r'http\:\/\/ws\.stream.+?\.m4a\?.+?(46)+?'
re_compile = re.compile(rex)
search = re_compile.search(content)
rehttp = re.compile(r'http://ws\.stream.+?/(\w+\.m4a)\?.+?46')
# 因为需要取得资源的名字，所以分个组更方便，但是只要有组的存在，findall就会只匹配组里的内容
# findall = rehttp.findall(content)
# print(findall)

finditer = rehttp.finditer(content)
for iter in finditer:
    print('url: %s       fileName: %s'%(iter.group(0), iter.group(1)))
