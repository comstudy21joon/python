# 함수의 결과값 여러개 전달

def getInfo() :
    return "HONG", "GILDONG", 33


def getInfo2() :
    return ("HONG", "GILDONG", 33)


def mkTuple(id, name, age) :
    return id, name, age


print(getInfo())

id, name, age = getInfo()
print(id, name, age)

tu = mkTuple("PARK", "GILSUN", 25)
print(tu)