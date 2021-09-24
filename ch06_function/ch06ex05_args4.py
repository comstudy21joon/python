
# findIndex 함수
# 리스트에서 값을 검색해서 몇번째 index에 존재 하는지 알아내는 함수 선언
def findIndex(list, value) :
    for i, in_list in enumerate(list) :
        try :
            in_list.index(value)
            return i
        except :
            continue

    return -1

index = findIndex([[1,2],[3,5],[100,2],[4, 6]], 100)
print("100은 %d번째 index이다." % index)
