# if ~ else 문을 이용한다.
# input 함수를 이용해서 정수를 입력 받고 홀수 인지 짝수 인지 판별
'''
number = int(input("정수를 입력 하세요: "))

print(number, ":", end=" ", sep=" ")

# 연산자 우선순위에 의해서 나머지 연산이 먼저 수행 된다.
if 0==number%2 :
    print("짝수입니다.")
else :
    print("홀수입니다.")
'''

# 연습문제)
# 정수를 입력 받아서 0이 아니고 3의 배수인지 판별하는 프로그램을 작성하세요.
integer = int(input("정수를 입력 하세요: "))
print(integer, ":", end=" ")

'''
if integer%3==0 and integer!=0 :
    print("3의 배수입니다.")
else :
    print("3의 배수가 아닙니다.")
'''
if integer == 0 :
    print("0입니다")
elif integer == 5 :
    print("5입니다")
elif integer%3==0 :    # else if가 아니다. elif이다.
    print("3의 배수입니다.")
else :
    print("3의 배수가 아닙니다.")
