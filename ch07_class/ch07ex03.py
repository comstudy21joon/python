class People :
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def greeting(self):
        return self.name + "님 안녕하세요!"

kim = People("KIM")
pList = [
    kim, People("LEE"), People("Park")
]

pList[0].setName("HONG")

for person in pList:
    print(person.greeting())