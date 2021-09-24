from phonebook.phonebook_module import *


# 메뉴 함수 선언
def menu():
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    no = int(input("선택>>> "))
    return no


def run(no):
    print("{}번이 선택되었습니다!".format(no))
    if no == 6:
        print("#### 종료 ####")
        exit(0)

    if no in range(1,len(factory)+1) :
        factory[no-1]()
    else :
        print("해당 사항 없슴");