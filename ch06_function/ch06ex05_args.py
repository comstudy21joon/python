# 함수에 여러 인수 전달 예제
# 호출시 여러개의 인수를 튜플형식의 매개변수로 받기
def findMax(*args) :
    print("args의 타입은:", type(args))

    max = 0
    for num in args :
        if num > max :
            max = num

    return max


# 호출 하는 함수에 하나이상 여러개의 인수를 가변적으로 전달 할수 있다.
maxinum = findMax(10)
print("가장 큰 수는 :", maxinum)

# 여러 인수를 튜블에 전달 한다
maxinum = findMax(2, 5, 10, 30, 100, 40, 7, 9)
print("가장 큰 수는 :", maxinum)











