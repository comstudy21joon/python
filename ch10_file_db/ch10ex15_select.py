import sqlite3
conn = sqlite3.connect('test.db')

sql = '''select * from saram'''
c = conn.cursor()
c.execute(sql)

print(c.fetchone())

# for s in c.fetchmany(10):
#     print(s)

for s in c.fetchall():
    print(s)

c.close()

conn.close()