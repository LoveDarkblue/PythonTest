import pickle

d = dict(name='tom', age=20)
dumps = pickle.dumps(d)  # 序列化
print(dumps)
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)  # 将序列化的内容保存到文件

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)  # 从文件中读取内容并反序列化成对象
    print(d, d['name'], d['age'])
