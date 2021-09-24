'''
print( type(365) )
print( type('hello') )
print( type(True) )
print( type([1,2,3,4]) )
print( type({'no':1, 'name':'kim'}) )
print( print )
'''

#print("Hello " + 5)



'''
str_full = input("문자열 입력>> ")
str_old = input("찾을 단어>> ")
str_new = input("바꿀 단어>> ")

start = str.index(str_old)
end = start + len(str_old)

result = str[:start] + str_new + str[end:]
print(result)
'''



'''
name = input("이름 입력>> ")
job = input("직업 입력>> ")
address = input("사는 곳>> ")
etc = input("특이 사항>> ")
print("{:-^60}".format("결과"))
print("이 름{:->50}".format("홍길동"))
print("직 업{:->50}".format("도둑"))
print("사는 곳{:->50}".format("서울시 종로구"))
print("특이 사항{:->50}".format("아버지를 아버지라 부르지 못함"))
'''


'''
name = input("성명 입력>> ")
age = input("나이 입력>> ")
address = input("주소 입력>> ")
print("{:-^40}".format("결과"))
print("%+15s : %s" %("user name", "홍길동"))
print("%+15s : %s" %("user age", 25))
print("%+15s : %s" %("user address", "한국 민속촌"))
'''

'''
jumin_num = input("주민 번호를 -를 포함해서 입력하라>> ")
idx = jumin_num.index('-')
jumin1 = jumin_num[:idx]
jumin2 = jumin_num[idx+1:]
print("주민번호 앞자리 : " + jumin1)
print("주민 번호 뒷 첫글자 : " + jumin2[0])
'''


decimal = int(input('정수 입력>> '))
print('2진수로 변환 => %s' %bin(decimal))
print('8진수로 변환 => %s' %oct(decimal))
print('16진수로 변환 => %s' %hex(decimal))






