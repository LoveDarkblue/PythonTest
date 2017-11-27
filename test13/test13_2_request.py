import requests

r = requests.get('https://www.baidu.com/')
print(r.status_code)
# print(r.text)
# keyfrom=Skykai521&key=977124034&type=data&doctype=json&version=1.1&q=name
d = {'keyfrom': 'Skykai521',
     'key': '977124034',
     'type': 'data',
     'doctype': 'json',
     'version': '1.1',
     'q': 'hello'}
r = requests.get('http://fanyi.youdao.com/openapi.do', params=d)
print(r.encoding)  # 自动检测编码
print(r.json())  # 直接输出json

r = requests.post('https:www.baidu.com/', data={'key': 'value'})

r = requests.post('https:www.baidu.com/', json={'key': 'value'})

r = requests.post('http://www.abc.com/', files={'file': open('co.jpg', 'rb')})

r = requests.get("http://www.abc.com/", timeout=5)

r = requests.get("https://www.baidu.com/", headers={'User-Agent': 'test', 'key': 'value'}, cookies={'key1': 'value'})

print(r.cookies)
print(r.cookies['BIDUPSID'])
