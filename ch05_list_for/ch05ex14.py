#폰북 리스트
pList = [
    {"name":"friend1", "phone":"010-1111-1111", "addr":"서울시 종로구"},
    {"name":"friend2", "phone":"010-2222-2222", "addr":"수원시 팔달구"},
    {"name":"friend3", "phone":"010-3333-3333", "addr":"부산시 사하구"},
    {"name":"friend2", "phone":"010-4444-4444", "addr":"광주시 송정동"},
    {"name":"friend4", "phone":"010-4444-4444", "addr":"광주시 송정동"}
]

while True:
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    no = int(input("선택: "))
    if no == 1 :
        print("{:-^50}".format(" 입력기능 "))
        # 친구 정보를 저장 하기위해 딕셔너리를 준비한다.
        people = {}
        # 딕셔너리에 키에 대응하는 값을 입력 받는다.
        people["name"] = input("성명>>> ")
        people["phone"] = input("전화>>> ")
        people["addr"] = input("주소>>> ")
        # 친구 정보가 저장 된 데이터를 리스트에 추가한다.
        pList.append(people)
        print("주소 입력 완료!")
    elif no == 2 :
        print("{:-^50}".format(" 출력기능 "))
        # 목록의 필드 제목을 출력 한다.
        print("{:^3}{:^10}{:^15}{:^20}".format("번호", "성명", "전화", "주소") )
        print("-"*53)
        # for 반복문을 이용해서 리스트의 내용을 화면에 출력한다.
        for i, p in enumerate(pList) :
            print("{:^3}{:^10}{:^15}{:^20}".format(i+1,p["name"],p["phone"],p["addr"]))
    elif no == 3 :
        print("{:-^50}".format(" 검색기능 "))
        # 검색 할 이름을 입력 받아서 변수에 저장한다.
        search_name = input("검색 할 이름 입력>>> ")
        # 입력 받은 내용이 없다면 다시 입력 받는다.
        while(len(search_name) == 0) :
            print("검색어를 1글자 이상 입력 하세요!")
            search_name = input("검색 할 이름 입력>>> ")
        # 중복된 이름이 있을 수 있기 때문에 검색한 데이터를 저장할 리스트를 준비한다.
        search_list = [];
        # 리스트의 내용을 하나씩 검색한다.
        for i, p in enumerate(pList) :
            # 검색어와 같은 이름이 있다면 미리 준비된 리스트에 추가 한다.
            if(p["name"] == search_name) :
                search_list.append(p);
        # 검색 내용이 없다면 검색 내용이 없다는 메세지를 출력한다.
        if(len(search_list) == 0) :
            print(search_name+"으로 검색 한 내용이 없습니다.")
        else :
            # 검색 내용이 있다면 검색 내용을 출력 한다.
            for i, p in enumerate(search_list) :
                print("{:^3}{:^10}{:^15}{:^20}".format(i+1,p["name"],p["phone"],p["addr"]))
    elif no == 4 :
        print("{:-^50}".format(" 수정기능 "))
        # 목록에서 수정 할 번호를 선택한다.
        modify_no = int(input("수정 할 번호 입력>>> "))
        # 리스트의 범위 보다 초과된 값이 입력되면 다시 입력 받도록 한다.
        while(modify_no<1 or modify_no>len(pList)) :
            print("입력 범위를 초과 했습니다!")
            modify_no = int(input("수정 할 번호 입력>>> "))
        # 목록의 인덱스르로 사용하기 위해서 번호-1을 한다. 인덱스튼 0부터 시작하기 때문이다.
        modify_no -= 1;
        # 성명, 전화번호, 주소 중에 수정 할 항목을 선택 한다.
        print("\n수정 할 항목을 입력 하세요.")
        print("1.성명 2.전화번호 3.주소 4.모두")
        modify_select = int(input("선택>>> "))
        if(modify_select == 1) :
            pList[modify_no]["name"] = input("새 이릅 입력>>> ")
        elif (modify_select == 2):
            pList[modify_no]["phone"] = input("새 전화번호 입력>>> ")
        elif (modify_select == 3):
            pList[modify_no]["addr"] = input("새 주소 입력>>> ")
        elif (modify_select == 4) :
            # 성명, 전화번호, 주소를 한꺼번에 수정 하는 메뉴
            pList[modify_no]["name"] = input("새 이릅 입력>>> ")
            pList[modify_no]["phone"] = input("새 전화번호 입력>>> ")
            pList[modify_no]["addr"] = input("새 주소 입력>>> ")
        else :
            print("선택 항목이 없습니다!")
    elif no == 5 :
        print("{:-^50}".format(" 삭제기능 "))
        # 목록에서 삭제할 번호를 입력 받는다.
        delete_no = int(input("삭제 할 번호 입력>>> "))
        # 목록의 수보다 초과된 값이 들어오면 다시 입력 받는다.
        while (delete_no < 1 or delete_no > len(pList)):
            print("입력 범위를 초과 했습니다!")
            delete_no = int(input("삭제 할 번호 입력>>> "))
        # 목록에서 해당 항목을 삭제한다.
        del pList[delete_no-1];
        print("삭제 완료 하였습니다!")
    elif no == 6 :
        print("{:-^50}".format(" 종료-굿바이 "))
        # 반복문을 탈출 하면 프로그램이 종료 된다.
        break
    else :
        print("{:-^50}".format(" 선택 사항 없슴 "))

    print() #공백 라인 추가

# end of while
print("다음 기회에 만나요~")