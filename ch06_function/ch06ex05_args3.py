
# 여러 인수를 딕셔너리로 전달 받는 함수 선언
def shwoDictArgs(**dictArgs) :
    print(dictArgs.values())
    keys = dictArgs.keys()
    for key in keys :
        print(key, ":", dictArgs[key])


shwoDictArgs(name="HONG", age=25, address="Seoul Korea")

