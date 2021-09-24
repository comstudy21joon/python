#딕셔너리 리스트
lis = []

for i in range(0,4) :
    people = {}
    people["name"] = input("성명>>> ")
    people["phone"] = input("전화>>> ")
    people["addr"] = input("주소>>> ")
    lis.append(people)

#print(lis)
for people in lis :
    #print(people)
    print("성명:{}, 전화:{}".format(people["name"],people["phone"]))