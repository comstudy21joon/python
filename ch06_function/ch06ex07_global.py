# 전역변수와 지역변수
from pprint import pprint

peoples = [
    {"num":1, "name":"KIM", "phone":"010-1111-1111"},
    {"num":2, "name":"LEE", "phone":"010-2222-2222"},
    {"num":3, "name":"PARK", "phone":"010-3333-3333"}
]

num_seq = 3

def addDictPeople(name, phone) :
    # 전역변수의 값을 변경 하려고 할때 global키워드를 이용해야한다.
    # 리스트에 내용을 추가하는것은 리스트 자체를 바꾸는게 아니므로 global없이 사용 가능.
    global num_seq
    num_seq += 1
    peoples.append({"num":num_seq, "name":name, "phone":phone})


addDictPeople("Ahn","010-4444-4444")
#print(peoples)
pprint(peoples)