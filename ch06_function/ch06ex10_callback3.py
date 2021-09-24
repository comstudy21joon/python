# 콜백함수 예제
def fncA() :
    print("fncA 함수를 실행합니다")


# 함수의 매개변수 전달
def otherFnc2(callback) :
    try :
        callback()
    except :
        print("함수가 아닙니다!")


otherFnc2(fncA)
otherFnc2(500)