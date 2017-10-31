import os

print(os.name)  # 操作系统类型
print(os.environ.get('CLASSPATH'))  # 获取系统中CLASSPATH环境变量的值
print(os.path.abspath('.'))  # 当前目录的绝对路径

# os.mkdir(os.path.join('/Python', 'TestDir'))  # 在根目录的Python目录下创建TestDir目录
# os.rmdir(os.path.join('/Python', 'TestDir'))  # 删除根目录下的Python目录下的TestDir目录

# print(os.path.split('/Python/TestDir'))  # 拆分路径
# print(os.path.splitext('/Python/TestDir/test9_1.py'))

# print(os.rename('/Python/TestDir/test9_1.py', '/Python/TestDir/test9_2.py'))

print([x for x in os.listdir('/Python') if os.path.isdir(os.path.join('/Python', ))])

print([f for f in os.listdir('.') if os.path.isfile(f) and os.path.splitext(f)[1] == '.py'])
