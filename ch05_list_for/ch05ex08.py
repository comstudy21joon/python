#딕셔너리 자료구조를 선언하고 사용 한다.
dic = {"name":"홍길동","phone":"010-1234-5678","addr":"서울시 은평구 응암동"}

name = dic.get("name")
phone = dic.get("phone")
addr = dic.get("addr")

print("Name: {}".format(name))
print("Phone: {}".format(phone))
print("Addr: {}".format(addr))