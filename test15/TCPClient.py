import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))  # 连接127.0.0.1主机的1234端口
print(s.recv(1024).decode('utf-8'))
for data in [b'AAA', '李'.encode('utf-8')]:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
