# 파일 열기
fp = open("io_test.txt", "w", encoding="utf-8")

# 파일에 내용 쓰기
fp.write("Hello World\n")
fp.write("건강한 대한민국\n")
fp.write("즐거운 파이썬 공부\n")

# 파일 닫기
fp.close()