# 다중 if문 예제
# 성적을 입력 받아서 학점을 환산한다
score = int(input("성적입력: "))
grade = 'F'

if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'

print("{}점은 {}학점이다".format(score, grade))