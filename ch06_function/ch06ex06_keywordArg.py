# 키워드 인수 호출

def showInofo(user, age, address) :
    print("User:", user)
    print("Age:", age)
    print("Address:", address)


# 매개변수의 위치를 기반으로 순서대로 인수를 전달한다.
showInofo("KIM", 25, "서울시 은평구")

# 매개변쉬의 위치와 관계없이 매개변수 이름을 키워드로 인수를 전달한다.
showInofo(address="서울시 구로구", age=26, user="PARK")
