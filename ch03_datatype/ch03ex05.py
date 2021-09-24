# format 함수를 이용한 문자열 처리
print("{:-^50}".format("사랑"))
print("{:&<50}".format("사랑"))
print("{:*>50}".format("사랑"))

name = "홍길동"
age = 45
info = "성명:{0} | 나이:{1}".format(name, age)
print(info)

