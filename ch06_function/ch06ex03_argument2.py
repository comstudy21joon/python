# 이름과 나이를 입력 받아 출력하는 함수 선언
def show_people(name, age) :
    print("[2] ", name, "님은 ",age ,"세입입니다", sep="")

# 함수를 호출 할때 함수의 매개변수 갯수만큰 인수를 전달해야 한다.
# 매개변수와 인수의 갯수가 다르면 실행시 오류가 발생 된다.
# 입력되는 인수는 매개변수가 선언된 순서대로 전달된다.
show_people("김길동", 25)