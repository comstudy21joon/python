# if문 예제
import sys

name = input("성명 입력: ")
if len(name) == 0 :
    print("성명을 입력 하지 않았습니다!")
    sys.exit()

print("당신의 이름은 {}이고 {}글자입니다.".format(name, len(name)))