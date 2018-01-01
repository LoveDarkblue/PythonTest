from wsgiref.simple_server import make_server

from test17.t17_2 import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
http = make_server('', 8000, application)
print('Serving HTTP on port 8000')
# 开始监听HTTP请求
http.serve_forever()
