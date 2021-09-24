# 성적을 score에 입력 받는다.
# 성적을 학점으로 환산해서 grade에 저장한다.
# score와 grade를 출력 한다.

# grade 변수를 'F'값으로 초기화 한다.

grade = 'F'
score = int(input("성적을 입력하세요: "))

# score<0 or score>100
while not(score in range(0,101)) :
    print("Error!")
    score = int(input("성적을 다시 입력하세요: "))

# 성적을 학점으로 환산 해 보세요. +=
if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'

# score의 1의 자리가 7보다크면 grade에 +를 붙이고 3보다 작으면 -를 붙인다.
num = score % 10
if num > 7 :
    grade = str(grade) + "+"
elif num < 3 :
    grade = str(grade) + "-"

print("{}점은 {}학점입니다.".format(score, grade))
