# 갈수 있는 나라 목록을 저장한다.
countryList = ["불란서","필리핀","대만","홍콩","미국","캐나다","베트남"]

journey = input("가고 싶은 여행지를 입력하세요: ")

'''
if journey in countryList :
    print("{}는 여행 가능한 여행지 목록에 있습니다.".format(journey))
else :
    print("{}는 여행 가능한 여행지 목록에 없습니다.".format(journey))
'''

while not(journey in countryList) :
    print("{}는 여행 가능한 여행지 목록에 없습니다.".format(journey))
    journey = input("가고 싶은 여행지를 다시 입력하세요: ")

print("{}는 여행 가능한 여행지 목록에 있습니다.".format(journey))