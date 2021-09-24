# 디폴트 매개변수 호출

def showInfo(id, name="no-name", age=0) :
    print("id:", id)
    print("name:", name)
    print("age:", age)


showInfo("HONG","GILDONG",25)
print("-"*30)
showInfo("KIM")
