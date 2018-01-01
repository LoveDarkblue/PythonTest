import sqlite3

dbName = 'test.db'


def createTab():
    connect = sqlite3.connect(dbName)
    cursor = connect.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT ,name VARCHAR(50),age INTEGER)')
    closeDb(connect, cursor)


def add():
    connect = sqlite3.connect(dbName)
    cursor = connect.cursor()
    cursor.execute('INSERT INTO student(name,age) VALUES (\'name2\',19)')
    print(cursor.rowcount)  # 影响的行数
    closeDb(connect, cursor)


def find():
    connect = sqlite3.connect(dbName)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM student')
    # cursor.execute('SELECT * FROM student WHERE age>?', (18,))
    print(cursor.fetchall())  # 获取查询的结果
    closeDb(connect, cursor)


def update():
    connect = sqlite3.connect(dbName)
    cursor = connect.cursor()
    cursor.execute('UPDATE student SET age=? WHERE name=?', (21, 'name2'))
    print(cursor.rowcount)
    closeDb(connect, cursor)


def delete():
    connect = sqlite3.connect(dbName)
    cursor = connect.cursor()
    cursor.execute('DELETE FROM student WHERE age>?', (19,))
    print(cursor.rowcount)  # 影响的行数
    closeDb(connect, cursor)


def closeDb(connect, cursor):
    cursor.close()
    connect.commit()
    connect.close()


find()
update()
find()
delete()
find()