# --------
# 람다 익명 함수 호출 할때 인수를 전달 해 본다.
fncList = [
    lambda msg : print(msg, '첫째 함수'),
    lambda msg : print(msg, '둘째 함수'),
    lambda msg : print(msg, '셋째 함수')
]

fncList[0]('hello')
fncList[1]('python')
fncList[2]('world')

