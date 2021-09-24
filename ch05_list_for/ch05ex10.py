# range() 함수를 이용한 for 반복문의 실행 예제
for i in range(5) :
    print(i, end=" ")

print()
# range() 함수의 입력 범위와 증가 값 설정
# range(시작값, 조료값, 증가값)
for num in range(3, 10, 2) :
    print(num, end=" ")

print()
# 꺼꾸로 감소하기
for cnt in range(10, 0, -1) :
    print(cnt, end=" ")