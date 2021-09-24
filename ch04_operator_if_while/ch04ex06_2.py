# 성명과 나이를 입력 받아서 출력 한다.
# 단, 성명을 입력받지 않으면 Error 메세지를 출력하고 즉시 종료한다.
# 나이를 입력 받아서 10년후 나이를 출력한다.
name = input("성명을 입력 하세요: ")

if len(name) == 0 :
    print("Error : 성명을 입력하지 않았습니다.")
else :
    age = int(input("나이를 입력 하세요: ") )
    print("당신의 이름은 {}입니다".format(name))
    print("당신은 10년후에 {}세입니다".format(age+10))

print("프로그램 종료!")