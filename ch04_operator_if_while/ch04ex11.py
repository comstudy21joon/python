'''
    1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료
    선택: 1
    ------- 입력기능 ----------

    1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료
    선택: 2
    ------- 출력기능 ----------

    1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료
    선택: 6
    ------- 프로그램 종료-굿바이 ----------
'''
while True:
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    no = int(input("선택: "))
    if no == 1 :
        print("{:-^50}".format(" 입력기능 "))
    elif no == 2 :
        print("{:-^50}".format(" 출력기능 "))
    elif no == 3 :
        print("{:-^50}".format(" 검색기능 "))
    elif no == 4 :
        print("{:-^50}".format(" 수정기능 "))
    elif no == 5 :
        print("{:-^50}".format(" 삭제기능 "))
    elif no == 6 :
        print("{:-^50}".format(" 종료-굿바이 "))
        break
    else :
        print("{:-^50}".format(" 선택 사항 없슴 "))

    print() #공백 라인 추가

# end of while
print("다음 기회에 만나요~")