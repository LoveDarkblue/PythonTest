from contextlib import contextmanager, closing
from urllib.request import urlopen

with open('test12_6_contextlib.py', 'r') as f:
    print(f.read(30))


# enter + exit
class TestContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('before')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def getName(self):
        print("TestContext name is %s" % self.name)


with TestContext('enter_exit') as t:
    t.getName()


# contextmanager
class TestContext1:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print("TestContext1 name is %s" % self.name)


@contextmanager
def getTestContext1Name(name):
    print('before')
    t = TestContext1(name)
    yield t
    print('end')


with getTestContext1Name('contextmanager') as t1:
    t1.getName()


@contextmanager
def htmTag(tagName):
    print("<%s>" % tagName)
    yield
    print("</%s>" % tagName)


with htmTag("div"):
    print('hello')
    print('python!')


@contextmanager
def myopen(filename, mode='r'):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()


with myopen('test12_6_contextlib.py', 'r') as f:
    print('myopen', f.name)

with closing(urlopen('https://www.python.org')) as page:
    for i in page:
        print(i)


@contextmanager
def closing(method):
    try:
        yield method
    finally:
        method.close()
