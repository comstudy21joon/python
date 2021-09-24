# 딕셔너리 클래스를 상속 받아서 변경 하기
class MyDict(dict) :
    def __init__(self):
        super().__init__()

    def setAttribute(self, key, value):
        self[key] = value

    def getAttribute(self, key):
        return self[key]

    def size(self):
        return len(self)

myDict = MyDict()
myDict.setAttribute("name", "hong-gildong")
myDict.setAttribute("address", "Seoul Korea")

print( myDict.getAttribute("name") )
print( myDict.getAttribute("address"))

print(myDict.size())
