import re

content = '''sadf123http://www.baidu.com/bg1.jgpsadfsdaf234http://www.baidu.com/bg1.jgpfdsa
'''
# 查找是否有满足正则的内容
rem = re.compile(r'http\:\/\/.+?/.+?\.[a-zA-Z]{3}')
search = rem.search(content)
print(search, type(search), search.group(0))
