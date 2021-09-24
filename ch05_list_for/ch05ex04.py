#리스트에 리스트를 연장한다.
li = ["홍길동", 23]
li.append("서울시 은평구")
li += ["aaa","bbb"]
li.append(["ccc","ddd"]) #중첩리스트
print(li)