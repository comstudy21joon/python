# 가고싶은 여행지를 입력 받아서 여행 가능 지역에 리스트에 있는지 검사한다.
countryList = ["유럽","필리핀","대만","캐나다","호주","미국","베트남"]
journey = input("가고 싶은 여행지를 입력 하세요: ")

if journey in countryList :
    print("{}는 여행 가능한 여행지에 있습니다".format(journey))
else :
    print("{}는 여행 가능한 여행지에 없습니다".format(journey))