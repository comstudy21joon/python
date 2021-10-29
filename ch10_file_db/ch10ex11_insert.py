import sqlite3
conn = sqlite3.connect('test.db')

sql = '''
    insert into saram(id, name, age) 
    values("park","gildong",34)
'''

# SQL문을 실행 해 줄 커서 객체를 생성한다.
c = conn.cursor()
c.execute(sql)
c.close()

# 트렌젝션을 commit한다.
conn.commit()
conn.close()