def comsumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('consumer---', n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('produce---', n)
        r = c.send(n)
        print('consumer return', r)
    c.close()


c = comsumer()
produce(c)
