import os

print(os.name)  # 操作系统类型
print(os.environ.get('CLASSPATH'))  # 获取系统中CLASSPATH环境变量的值
print(os.path.abspath('.'))  # 当前目录的绝对路径
