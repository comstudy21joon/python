import  datetime

print("어서오세요.")
# 성명을 입력 받아서 user_name 변수에 저장한다.
user_name = input("성명을 입력 하세요 >> ")
# 입력 된 성명을 출력 한다.
print("%s님 안녕하세요" %user_name)
# 생년을 입력 받는다.
birth_year = int(input("생년을 입력 하세요(예: 1991) >> "))
# 현재 날짜를 str_today 변수에 저장한다.
str_today = str(datetime.date.today())
# 현재 날짜에서 연도만 추출한다.
now_year = int(str_today.split('-')[0])
# 현재 년도에서 생년을 빼면 나이가 된다.
age = now_year-birth_year
# 현재 연도와 사용자의 나이를 출력한다.
print("%s님은 %d년 현재 %d세입니다. \n" %(user_name, now_year, age))
# 제어문을 이용해서 미성년자인지 성인인지 구분한다.
if(age < 19) :
    print("%s님은 미성년자입니다." %user_name)
else :
    print("%s님은 성인입니다." %user_name)
