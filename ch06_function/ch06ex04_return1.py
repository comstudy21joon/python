# 함수 처리 결과 값 돌려주기
# 함수에서 처리한 결과 값을 함수가 호출된 지점으로 돌려 줄 수 있다.
# 함수는 처리할 인수를 전달 받고 그 결과를 반환하는 일을 한다.


# 두개의 정수를 입력 받아 비교 후 더 큰수를 반환 해주는 함수 선언 예제
def get_max(num1, num2) :
    if num1 > num2 :
        maxinum = num1
    else :
        maxinum = num2

    return maxinum

# 더 큰수를 찾아주는 함수에 두개의 인수 전달.
result = get_max(10, 100)
print("더 큰수는 {}입니다!".format(result))
