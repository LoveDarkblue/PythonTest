import threading

std_local = threading.local()

class Student:
    def __init__(self, name):
        self.name = name


def pri():
    print(std_local.std.name)  # 取出对应线程的student对象


def stdthread(str):
    std = Student(str)
    std_local.std = std
    pri()


def thread_test():
    t1 = threading.Thread(target=stdthread, args=('Tom',), name='Thread-1')
    t2 = threading.Thread(target=stdthread, args=('Mary',), name='Thread-2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


thread_test()
