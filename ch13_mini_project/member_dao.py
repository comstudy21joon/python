import sqlite3

db_file = 'members.db'
sql_select_all = '''select * from member'''
sql_select = '''select * from member where name="%s"'''
sql_create = '''create table IF NOT EXISTS member(
    no integer primary key,
    name varchar(20),
    phone varchar(20),
    email varchar(20))'''
sql_insert = '''insert into member(name, phone, email) values(?,?,?)'''
sql_delete = '''delete from member where no=%s'''
sql_update = '''update member set name='%s', phone='%s', email='%s' where no=%s'''


def create_table() :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.execute(sql_create)

    c.close()
    conn.close()
    #print('테이블 생성 성공!')


def select_all() :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.execute(sql_select_all)

    list = []
    for s in c.fetchall():
        list.append(s)

    c.close()
    conn.close()

    return list


def select(name) :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.execute(sql_select %name)

    list = []
    for s in c.fetchall():
        list.append(s)

    c.close()
    conn.close()

    return list


def insert_many(data_list) :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.executemany(sql_insert, data_list)
    c.close()

    conn.commit()
    conn.close()


def insert(tuple_data) :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.execute(sql_insert, tuple_data)
    c.close()

    conn.commit()
    conn.close()


def delete(no) :
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    c.execute(sql_delete %no)
    c.close()

    conn.commit()
    conn.close()


def update(tuple_data) :
    conn = sqlite3.connect(db_file)
    # name, phone, email, no
    c = conn.cursor()
    c.execute(sql_update %tuple_data)
    c.close()

    conn.commit()
    conn.close()