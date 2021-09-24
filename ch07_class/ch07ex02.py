def setName(name=None, self=None) :
    self["name"] = name

person = {
    "name" : "HONG",
    "setName" : setName,
    "greeting" : (lambda : person['name'] + "님 안녕하세요!")
}

print(person['greeting']())
person['setName']('KIM', person)
print(person['greeting']())