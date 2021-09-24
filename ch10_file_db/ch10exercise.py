'''
members = []

while True :
    no = int(input('(1)입력 (2)출력 (3)저장 (4)불러오기 (5)종료 >> '))
    if no == 1 :
        print('--- 입력 기능 ---')
        member = {}
        member['name'] = input('성명입력 >> ')
        member['phone'] = input('전화번호 >> ')
        members.append(member)
        print('입력 완료!')
    elif no == 2 :
        print("--- 출력 기능 ---")
        for member in members :
            print('%-10s%-20s\n' %(member['name'], member['phone']))
        print('출력 완료!')
    elif no == 3 :
        print("--- 저장 기능 ---")

    elif no == 4 :
        print("--- 불러오기 기능 ---")

    elif no == 5 :
        break
    else :
        print('해당 사항 없습니다.')

print("종료합니다!")
'''
from pprint import pprint

'''
import pickle

members = []

while True :
    no = int(input('(1)입력 (2)출력 (3)저장 (4)불러오기 (5)종료 >> '))
    if no == 1 :
        print('--- 입력 기능 ---')
        member = {}
        member['name'] = input('성명입력 >> ')
        member['phone'] = input('전화번호 >> ')
        members.append(member)
        print('입력 완료!')
    elif no == 2 :
        print("--- 출력 기능 ---")
        for member in members :
            print('%-10s%-20s' %(member['name'], member['phone']))

        print('출력 완료!')
    elif no == 3 :
        print("--- 저장 기능 ---")
        with open('members.pickle', 'wb') as f:
            pickle.dump(members, f)

        print('저장 완료!')
    elif no == 4 :
        print("--- 불러오기 기능 ---")
        with open('members.pickle', 'rb') as f:
            members = pickle.load(f)

        print('불러오기 완료!')
    elif no == 5 :
        break
    else :
        print('해당 사항 없습니다.')

print("종료합니다!")
'''




'''
import json

members = []

while True :
    no = int(input('(1)입력 (2)출력 (3)저장 (4)불러오기 (5)종료 >> '))
    if no == 1 :
        print('--- 입력 기능 ---')
        member = {}
        member['name'] = input('성명입력 >> ')
        member['phone'] = input('전화번호 >> ')
        members.append(member)
        print('입력 완료!')
    elif no == 2 :
        print("--- 출력 기능 ---")
        for member in members :
            print('%-10s%-20s' %(member['name'], member['phone']))

        print('출력 완료!')
    elif no == 3 :
        print("--- 저장 기능 ---")
        with open('members.json', 'w') as f:
            json.dump(members, f)

        print('json 저장 완료!')
    elif no == 4 :
        print("--- 불러오기 기능 ---")
        with open('members.json', 'r') as f:
            members = json.load(f)

        print('json 불러오기 완료!')
    elif no == 5 :
        break
    else :
        print('해당 사항 없습니다.')

print("종료합니다!")
'''



"""
import sqlite3

# dB에 테이블이 없다면 새 테이블 생성
conn1 = sqlite3.connect('test.db')
sql = '''
create table IF NOT EXISTS members(
    no integer primary key,
    name varchar(10),
    phone varchar(20)
)
'''
c = conn1.cursor()
c.execute(sql)
c.close()
conn1.close()

# 멤버 정보를 저장 할 리스트
members = []

while True :
    no = int(input('(1)입력 (2)출력 (3)저장 (4)불러오기 (5)종료 >> '))
    if no == 1 :
        print('--- 입력 기능 ---')
        member = {}
        member['name'] = input('성명입력 >> ')
        member['phone'] = input('전화번호 >> ')
        members.append(member)
        print('입력 완료!')
    elif no == 2 :
        print("--- 출력 기능 ---")
        for member in members :
            print('%-10s%-20s' %(member['name'], member['phone']))

        print('출력 완료!')
    elif no == 3 :
        print("--- 저장 기능 ---")
        conn = sqlite3.connect('test.db')
        sql = '''
            insert into members(name, phone)
            values(?,?)
            '''
        c = conn.cursor()
        
        c.execute('delete from members')
        
        data = []
        for mem in members :
            list = []
            list.append(mem['name'])
            list.append(mem['phone'])
            data.append(tuple(list))

        c.executemany(sql, data)
        c.close()
        conn.commit()
        conn.close()

        print('데이터베이스 저장 완료!')
    elif no == 4 :
        print("--- 불러오기 기능 ---")
        conn = sqlite3.connect('test.db')

        sql = '''select * from members'''
        c = conn.cursor()
        c.execute(sql)

        members.clear()
        for s in c.fetchall():
            dic = {'name':s[1], 'phone':s[2]}
            members.append(dic)

        c.close()
        conn.close()

        print('데이터베이스 불러오기 완료!')
    elif no == 5 :
        break
    else :
        print('해당 사항 없습니다.')

print("종료합니다!")

"""




"""
import sqlite3

# dB에 테이블이 없다면 새 테이블 생성
conn1 = sqlite3.connect('test.db')
sql = '''
create table IF NOT EXISTS members(
    no integer primary key,
    name varchar(10),
    phone varchar(20)
)
'''
c = conn1.cursor()
c.execute(sql)
c.close()
conn1.close()

# 멤버 정보를 저장 할 리스트
members = []

while True :
    no = int(input('(1)입력 (2)출력 (3)검색 (4)수정 (5)삭제 (6)종료 >> '))
    if no == 1 :
        print('--- 입력 기능 ---')
        conn = sqlite3.connect('test.db')
        sql = '''
                    insert into members(name, phone)
                    values(?,?)
                    '''
        c = conn.cursor()
        data = (input('성명입력 >> '), input('전화번호 >> '))

        c.execute(sql, data)
        c.close()
        conn.commit()
        conn.close()

        print('입력 완료!')
    elif no == 2 :
        conn = sqlite3.connect('test.db')

        sql = '''select * from members'''
        c = conn.cursor()
        c.execute(sql)

        members.clear()
        for s in c.fetchall():
            dic = {'name': s[1], 'phone': s[2]}
            members.append(dic)

        c.close()
        conn.close()

        print("--- 출력 기능 ---")
        for member in members :
            print('%-10s%-20s' %(member['name'], member['phone']))

        print('출력 완료!')
    elif no == 3 :
        print("--- 검색 기능 ---")
        sname = input("검색 할 이름 입력 >> ")

        conn = sqlite3.connect('test.db')

        sql = '''select * from members where name="{}"'''
        c = conn.cursor()
        c.execute(sql.format(sname))

        mem = c.fetchone()
        print(mem)

        c.close()
        conn.close()
    elif no == 4 :
        print("--- 수정 기능 ---")
        sname = input("수정 할 이름 입력 >> ")

        conn = sqlite3.connect('test.db')
        sql = '''select * from members where name="{}"'''
        c = conn.cursor()
        c.execute(sql.format(sname))

        mem = c.fetchone()
        if mem == None :
            print('수정 할 대상이 없습니다!')
        else :
            print(mem)
            new_name = input('새이름 >> ')
            new_phone = input('새번호 >> ')

            sql2 = '''update members set name="{}", phone="{}" where name="{}"'''
            c.execute(sql2.format(new_name, new_phone, sname))
            conn.commit()
            print('수정 완료!')

        c.close()
        conn.close()


    elif no == 5 :
        print("--- 삭제 기능 ---")
        sname = input("삭제 할 이름 입력 >> ")

        conn = sqlite3.connect('test.db')
        sql = '''select * from members where name="{}"'''
        c = conn.cursor()
        c.execute(sql.format(sname))

        mem = c.fetchone()
        if mem == None:
            print('수정 할 대상이 없습니다!')
        else:
            print(mem)
            sql2 = '''delete from members where name="{}"'''
            c.execute(sql2.format(sname))
            conn.commit()
            print('삭제 완료!')

        c.close()
        conn.close()

    elif no == 6 :
        break
    else :
        print('해당 사항 없습니다.')

print("종료합니다!")



sql = '''select * from members where name="{}"'''
c = conn.cursor()
c.execute(sql.format(sname))

mem = c.fetchone()
if mem == None:
    print('수정 할 대상이 없습니다!')
else:
    print(mem)
    sql2 = '''delete from members where name="{}"'''
    c.execute(sql2.format(sname))
    conn.commit()
    print('삭제 완료!')
"""




import json

# 저장된 데이터를 읽는다.
with open('contacts.json', 'r') as f:
    obj = json.load(f)


# 읽어 들인 JSON객체에서 리스트를 가져온다.
contacts = obj['contacts']

# 리스트를 출력 한다.
print("%-7s%-20s%-40s%-20s" %('id','name','address','email'))
for mem in contacts :
    id = mem['id']
    name = mem['name']
    address = mem['address']
    email = mem['email']
    print("%-7s%-20s%-40s%-20s" %(id, name, address, email))

