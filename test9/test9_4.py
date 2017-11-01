import json


# d = dict(name='tom', age=20)
# dumps = json.dumps(d)  # 序列化
# print(dumps)
#
# loads = json.loads(dumps)  # 反序列化成对象
# print(loads)
# print(type(loads))


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def person2json(person):
    return {
        'name': person.name,
        'age': person.age
    }


p = Person('Mary', 20)
dumps = json.dumps(p, default=person2json)
print(dumps, type(dumps))


def json2person(d):
    return Person(d['name'], d['age'])


p1 = json.loads(dumps, object_hook=json2person)
print(p1, p1.name)


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student('Mary', 20)
json_dumps = json.dumps(s, default=lambda obj: obj.__dict__)
print(json_dumps, type(json_dumps))
