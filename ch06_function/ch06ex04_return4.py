# 성명, 나이, 주소를 입력 받아서 리스트로 만들어주는 함수
def mkPersonList() :
    newList = []
    newList.append(input("성명을 입력 하세요:  "))
    newList.append(input("전화번호 입력 하세요:  "))
    newList.append(input("주소를 입력 하세요:  "))

    return newList

# 함수에서 반환된 리스트를 저장하는 리스트
personList = mkPersonList()
for person in personList:
    print(person)