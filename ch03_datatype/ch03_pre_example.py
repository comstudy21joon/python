# 프로그램 제목을 콘솔에 출력 합니다.
print("::: 고객 정보 입력 :::")
# 고객 정보를 입력 받아서 각각 변수에 저장 합니다.
user_name = input("고객명 입력 >> ")
age = int(input("나이 입력 >> "))
email = input("이메일 입력 >> ")
phone = input("전화번호 입력 >> ")
# 입력 받은 고객 정보를 콘솔에 출력 합니다.
# 문자열의 format() 메소드를 이용해서 좀더 보기 좋게 출력 해 줍니다.
print("{:-^60}".format(" 입력 결과 "))
print("{: ^10}|{: ^5}|{: ^20}| {: ^20}".format("name", "age", "email", "phone"))
print("-"*65)
print("{: ^10}|{: ^5}|{: ^20}| {: ^20}".format(user_name, age, email, phone))