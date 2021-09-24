# 콜백함수 예제
def fncA() :
    print("fncA 함수를 실행합니다")


# 함수의 매개변수 전달
def otherFnc(callback) :
    #print(type(callback))
    #print(str(type(callback)) == "<class 'function'>" )
    if str(type(callback)) == "<class 'function'>" :
        fncA()
    else :
        print(callback,"은 함수가 아닙니다!")

otherFnc(fncA)
otherFnc(500)
