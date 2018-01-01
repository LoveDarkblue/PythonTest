import socket
import threading

import time


def tcplink(sock, addr):
    print('Accept new connecting from %s:%s' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(10)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connect from %s:%s closed!' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个socket
s.bind(('127.0.0.1', 1234))  # 绑定ip和端口
s.listen(2)  # 最多连接两个客户端,如果已经建立了两个连接，第三个客户端来再连接就得等待已连接的客户端断开后才能连接上
print('Waiting for connection...')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink(sock, addr))
