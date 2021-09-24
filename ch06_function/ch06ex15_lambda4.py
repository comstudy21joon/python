# -------
# 람다 익명 함수를 리스트에 담아서 사용 해 본다
fncList = [
    lambda : print('첫째 함수'),
    lambda : print('둘째 함수'),
    lambda : print('셋째 함수')
]

fncList[0]()
fncList[1]()
fncList[2]()
