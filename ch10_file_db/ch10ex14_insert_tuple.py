import sqlite3
conn = sqlite3.connect('test.db')

sql = '''
insert into saram(id, name, age)
values(?,?,?)
'''
c = conn.cursor()
c.execute(sql, ('lee','gilsun',21))
c.close()

conn.commit()
conn.close()