import asyncio


@asyncio.coroutine
def method1(host):
    print('get %s' % host)
    connection = asyncio.open_connection(host, 80)
    reader, writer = yield from connection
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


loop = asyncio.get_event_loop()
tasks = [method1(host) for host in ("www.163.com", "www.baidu.com", "www.sina.com.cn")]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
