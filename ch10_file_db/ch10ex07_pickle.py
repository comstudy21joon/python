# pickle 모듈을 불러온다.
import pickle

# 딕셔너리 객체 데이터
from pprint import pprint

person1 = {
    'name':'홍길순',
    'height':170,
    'weight':60
}

person2 = {
    'name':'홍길동',
    'height':200,
    'weight':80
}

# 딕셔너리 객체 데이터를 리스트로 만든다.
people = [person1, person2]

# 데이터를 저장한다.
# pickle은 바이너리로 저장 되므로 'wb'모드로 파일을 열어야 한다.
with open('people.pickle', 'wb') as f:
    pickle.dump(people, f)


# 저장된 데이터를 읽는다.
with open('people.pickle', 'rb') as f:
    loaded_people = pickle.load(f)

pprint(loaded_people)