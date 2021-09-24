# input으로 입력받는것은 무조건 문자열 타입이다.
# 숫자 타입은 int()함수 또는 float()함수로 현변환 해야 한다.
num1 = int( input("num1 입력 : ") )
print( type(num1) )

# 정수 두개를 키보드로 입력 받아서 더하는 프로그램
a = int(input("정수 a입력 : "))
b = int(input("정수 b입력 : "))
result = a + b
print("{} + {} = {}".format(a, b, result))