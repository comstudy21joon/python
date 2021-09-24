# 앞의 함수를 람다식으로 바꾸면 아래와 같다.
# 표현식에는 삼항연산자를 사용 했다.
# 참일때결과 if 조건식 else 거짓일때결과
result = (lambda x,y : x if x>y else y)(5,10)
print("result => ", result)
