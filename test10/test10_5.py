import threading

lock = threading.Lock()


# lock = threading.Lock()

def methodRun():
    lock.acquire()#获取锁
    try:
        print('thread %s is running...' % threading.current_thread().name)
    finally:
        lock.release()#释放锁


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=methodRun, name='ChildThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
