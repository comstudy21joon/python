#리스트의 선언
#lis = list()
lis = []
#리스트의 각각 요소는 타입이 다를수 있다.
lis.append("홍길동")
lis.append("김길동")
lis.append(100)
lis.append(200)
lis.append(3.14)
print(type(lis) )
print(lis)
#리스트에 없은 요소를 index() 함수로 검색하면 ValueError 발생
#print(lis.index(1000))
# 리스트의 범위를 넘은 첨자를 사용 해도 IndexError 발생
#print(lis[10])