
'''
3. 인덱싱을 이용해서 새로운 문자열 만들기
str2 = "Hello world!"
str2를 "Hello Python world!"로 변경 하고 싶다면?
'''

str2 = "Hello world!"
idx = str2.index("world")
print(str2[:idx])
print(str2[idx:])

str2 = str2[:idx] + "Python " + str2[idx:]
print(str2)

# 인덱스에 음수를 사용하면 문자열 끝에서 부터 인덱싱한다.
print(str2[2:-3])
