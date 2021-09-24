# 콜백함수 람보 구현 예제
def ramboAction(callback) :
    try :
        print("람보 액션!")
        callback("람보")
        print("-"*20)
    except :
        print("함수가 아닙니다")


def gun(user) :
    print(user + "가 총을 쏜다~ 탕탕탕!")


def sword(user) :
    print(user + "가 검을 휘두른다~ 휙휙휙!")


ramboAction(gun)
ramboAction(sword)
