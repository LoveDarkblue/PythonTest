import hashlib

md5 = hashlib.md5()
md5.update("testtest".encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update("test".encode('utf-8'))
md5.update("test".encode('utf-8'))
print(md5.hexdigest())
