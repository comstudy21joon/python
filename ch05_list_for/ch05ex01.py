# 리스트 선언 및 초기화
movieList = ["시네마천국","삼국지","혹성탈출","태권V","기생충"]
# movieList 의 구조
print("0. 리스트의 구조 :", movieList)
# 리스트의 첫번째 요소와 마지막 요소 확인
print("1. 리스트의 첫번째 요소 :", movieList[0])
print("2. 리스트의 마지막 요소 :", movieList[len(movieList)-1])
# 리스트의 요소값 변경
movieList[1] = "아이언맨"
print("3. 요소 변경 후 리스트의 구조 :", movieList)
# 리스트의 요소 삭제
del movieList[2]
print("4. 요소 삭제 후 :", movieList)
# 리스트 맨뒤에 새 요소 추가
movieList.append("쿵푸허슬")
print("5. 새 요소 추가 후 :", movieList)
# 리스트 중간에 새 요소 추가
movieList.insert(2, "올드보이")
print("6. 중간에 새 요소 추가 후 :", movieList)
# 리스트에서 요소의 위치 확인
print("7. 요소의 위치 확인 :", movieList.index("아이언맨"))