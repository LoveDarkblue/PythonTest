import asyncio

@asyncio.coroutine
def method1():
    print('method1_0')
    r = yield from asyncio.sleep(1);
    print('method1_1')

@asyncio.coroutine
def method2():
    print('method2_0')
    r = yield from asyncio.sleep(1);
    print('method2_1')


loop = asyncio.get_event_loop()
tasks = [method1(), method2()]
# loop.run_until_complete(method1())
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
