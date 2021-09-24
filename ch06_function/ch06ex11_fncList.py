# 함수를 담는 리스트

def fncA() :
    print("첫번째 함수 실행 됨")

def fncB() :
    print("두번째 함수 실행 됨")

def fncC() :
    print("세번째 함수 실행 됨")

factory = [fncA, fncB, fncC ]

factory[0]()
factory[1]()
factory[2]()

print("-" * 30)

for fnc in factory :
    fnc()

