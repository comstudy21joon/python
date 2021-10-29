import sqlite3
conn = sqlite3.connect('test.db')

sql = '''
    create table IF NOT EXISTS saram(
    no integer primary key,
    id varchar(20),
    name varchar(20),
    age integer
)
'''
c = conn.cursor()
c.execute(sql)

c.close()
conn.close()