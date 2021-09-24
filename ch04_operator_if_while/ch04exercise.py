'''
print("줄 바꿈 문자는 \\n인데 이를 \"개행문자\"라고 한다.")
print('줄 바꿈 문자는 \\n인데 이를 "개행문자"라고 한다.')
'''

'''
print("정수를 입력 하면 양수, 음수, 0을 판별합니다.")
integer = int(input('정수 입력>> '))
if integer > 0 :
    print("양수입니다")
elif integer < 0 :
    print("음수입니다")
else :
    print("0입니다")
'''


'''
print("금액을 입력 받아서 돈의 종류별 개수를 환산하는 프로그램")
won_total = int(input('금액 입력>> '))
remainder = won_total
won50000 = remainder // 50000
remainder = remainder % 50000
won10000 = remainder // 10000
remainder = remainder % 10000
won5000 = remainder // 5000
remainder = remainder % 5000
won1000 = remainder // 1000
remainder = remainder % 1000
won500 = remainder // 500
remainder = remainder % 500
won100 = remainder // 100
remainder = remainder % 100
won50 = remainder // 50
remainder = remainder % 50
won10 = remainder // 10
remainder = remainder % 10
won5 = remainder // 5
remainder = remainder % 5
won1 = remainder;

print("{:-^20}".format("결과"))
print("오만원권 : {}매".format(won50000))
print("만원권 : {}매".format(won10000))
print("오천원권 : {}매".format(won5000))
print("천원권 : {}매".format(won1000))
print("오백원 : {}개".format(won500))
print("백원 : {}개".format(won100))
print("오십원 : {}개".format(won50))
print("십원 : {}개".format(won10))
print("오원 : {}개".format(won5))
print("월 : {}개".format(won1))
'''


'''
city = input('사는 도시 입력>> ')

if city == '서울' :
    print(city+'는 특별시 입니다.')
elif city in ['대전','대구','부산','광주','울산','인천'] :
    print(city + '는 광역시입니다')
else :
    print(city + '는 특별시나 광역시가 아닙니다')
'''

'''
word = input('검색어 입력>> ')
if len(word) < 3 :
    print('검색어가 너무 짧습니다.')
elif len(word) >= 10 :
    print('검색어가 너무 깁니다.')
else :
    print('입력 한 검색어는 '+word+'입니다.')
'''

'''
while True :
    word = input('검색어 입력>> ')
    if word == '그만' : break
    if len(word) < 3:
        print('검색어가 너무 짧습니다.')
    elif len(word) >= 10:
        print('검색어가 너무 깁니다.')
    else:
        print('입력 한 검색어는 ' + word + '입니다.')

print('검색어 입력 프로그램을 종료 합니다.')
'''

yn = 'y'
while yn == 'y' :
    name = input('성명 입력>> ')
    major = input('전공 입력>> ')
    print(name+"님의 전공은 " +major+ "입니다.")
    yn = input('계속 하시겠습니까(y또는n입력) >>')
    while not(yn in ['y','n']) :
        print('y또는 n만 입력 하세요.')
        yn = input('계속 하시겠습니까(y또는n입력) >>')



