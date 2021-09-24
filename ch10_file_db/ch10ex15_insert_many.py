import sqlite3
conn = sqlite3.connect('test.db')

sql = '''
insert into saram(id, name, age)
values(?,?,?)
'''

data = [
    ('kim','gisu',11),
    ('cho','gildong',21),
    ('nam','gildong',31)
]

c = conn.cursor()
c.executemany(sql, data)
c.close()

conn.commit()
conn.close()