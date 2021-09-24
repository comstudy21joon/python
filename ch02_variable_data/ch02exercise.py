'''
# 1. 성적 출력
print("성적 출력 프로그램입니다.")
name = input("셩명 입력>> ")
kor = int(input("국어 성적>> "))
eng = int(input("국어 성적>> "))
mat = int(input("국어 성적>> "))

total = kor + eng + mat
avg = total // 3.0;

print("--- 계산 결과 ---")
print("성명 : " + name)
print("국어 : " + str(kor))
print("영어 : " + str(eng))
print("수학 : " + str(mat))
print("총점 : " + str(total))
print("평균 : " + str(avg))
'''


'''
print("원의 둘레와 넓이를 구하는 프로그램")
PI = 3.141592
r = int(input("원의 반지름 입력>> "))
line = 2 * PI * r
area = PI * r * r
print("반지름이 {}인 원의 둘레의 길이는 {}이고 넓이는 {}이다.".format(r, line, area))
'''

'''
print("3개의 정수를 입력 받아서 가장 큰 수와 가장 작은 수를 구하는 프로그램")
a = int(input('첫번째 정수 입력>> '))
b = int(input('두번째 정수 입력>> '))
c = int(input('세번째 정수 입력>> '))

max_num = max(a, max(b, c))
min_num = min(a, min(b, c))

print("{:-^30}".format('결과'))
print("가장 큰 수는 %d입니다." %max_num)
print("가장 작은 수는 %d입니다." %min_num)
'''


'''
print("평을 입력 받아서 몇 제곱미터인지 환산하는 프로그램")
p = int(input("평 입력>> "))
mm = p * 3.3058
print("{}평은 {}제곱미터이다.".format(p, mm))
'''

'''
#이름, 이메일, 전화번호, 주소를 입력 받아서 한 줄에 출력
print("이름, 이메일, 전화번호, 주소를 입력 받는 프로그램")
name = input("이름 입력>> ")
email = input("이메일 입력>> ")
phone = input("전화번호 입력>> ")
addr = input("주소 입력>> ")

print("{:-^30}".format('결과'))
print("%-10s %-20s %-20s %-20s" %("name", "email", "phone", "address"))
print("%-10s %-20s %-20s %-20s" %(name, email, phone, addr))
'''

print("%.2f" %3.141592)