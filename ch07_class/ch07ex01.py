test={ "name" : "HONG" }

def getName(self=test) :
    return self["name"]

def setName(name=None, self=test) :
    self["name"] = name

test['getName'] = getName;
test['setName'] = setName;

print("이름은 ", test['getName']())
test["setName"]("KIM")
print("변경된 이름은 ", test['getName']())