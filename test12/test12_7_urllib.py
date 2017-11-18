from urllib import request, parse

et
with request.urlopen('http://www.sojson.com/open/api/weather/json.shtml?city=%s' % parse.quote("北京")) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('response:', data.decode('utf-8'))

# request_request = request.Request('https://www.baidu.com/')
# request_request.add_header('User-Agent', 'Test')  # 给请求增加header参数
# request_request.add_header('token', '123456')
# with request.urlopen(request_request) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('response:', f.read().decode('utf-8'))

st
params = parse.urlencode([
    ('key1', 'value1'),
    ('key2', 'value2')])
req_post = request.Request('http://www.baidu.com')
with request.urlopen(req_post,data=params.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
for k, v in f.getheaders():
    print('%s: %s' % (k, v))
print('Data:', f.read().decode('utf-8'))

