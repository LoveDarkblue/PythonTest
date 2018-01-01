import socket
import threading

import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 1234))  # 绑定ip和端口，不需要listen，直接接收来自任何客户端的数据
print('bind udp on 1234...')
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s' % addr)
    s.sendto(b'Hello,%s!' % data, addr)
