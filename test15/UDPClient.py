import socket
import threading

import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'AAA', b'BBB']:
    s.sendto(data, ('127.0.0.1', 1234))
    print(s.recv(1024).decode('utf-8'))
s.close()
