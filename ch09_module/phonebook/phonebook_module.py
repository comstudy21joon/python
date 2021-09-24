from phonebook.phonebook_data import *


# 기능별 함수 선언
def mkData():
    # 성명, 전화번호, 주소를 입력받아서 돌려주는 함수
    global idx
    idx += 1
    name = input("성명입력>>> ")
    phone = input("전화번호입력>>> ")
    addr = input("주소입력>>> ")

    return {"idx": idx, "name": name, "phone": phone, "addr": addr}


def inputData():
    print("#### 입력 기능 ####")
    # 입력 기능을 구현 해 보세요.
    data_value = mkData()
    addrList.append(data_value)
    print("데이터 입력 성공!")


def outputData():
    print("#### 출력 기능 ####")
    for person in addrList:
        print("{: ^3}|{: ^6}|{: ^13}|{: ^9}".format(person["idx"], person["name"], person["phone"], person["addr"]))


def find_idx(addrList, idx=None, name=None):
    flag = 0
    if name != None:
        flag = 1

    for i, person in enumerate(addrList):
        if flag == 0:
            if person["idx"] == idx:
                return i
        else:
            if person["name"] == name:
                return i

    # for문 밖으로 나온것은 대상이 없다는 의미
    return -1


def searchData():
    print("#### 검색 기능 ####")
    searchName = input("검색 할 이름을 입력하세요 : ")
    index = find_idx(addrList, name=searchName)
    person = addrList[index]
    print("{: ^3}|{: ^6}|{: ^13}|{: ^9}".format(person["idx"], person["name"], person["phone"], person["addr"]))


def modifyData():
    print("#### 수정 기능 ####")


def deleteData():
    print("#### 삭제 기능 ####")
    # del addrList[1]
    del_idx = int(input("삭제 할 번호를 입력 하세요 : "))
    index = find_idx(addrList, idx=del_idx)
    if index != -1:
        del addrList[index]
        print("삭제 성공!")
    else:
        print("삭제 할 대상이 없습니다!")

factory = [inputData, outputData, searchData, modifyData, deleteData]