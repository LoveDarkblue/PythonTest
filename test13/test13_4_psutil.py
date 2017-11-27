import psutil

print(psutil.cpu_count())  # CPU逻辑数量
print(psutil.cpu_count(logical=False))  # CPU物理核心
print(psutil.cpu_times())  # CPU 的用户、系统、空闲时间

print(psutil.virtual_memory())  # 物理内存信息

print(psutil.disk_partitions())  # 磁盘信息
print(psutil.disk_usage('/'))  # 路径所在磁盘内存使用情况
