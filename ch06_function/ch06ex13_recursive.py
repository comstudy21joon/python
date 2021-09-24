# 재귀호출 예제
def subRecursive(i) :
    if i > 0 :
        print("-"*i)
        subRecursive(i-2)
    else :
        return

def recursive(i) :
    if i > 0 :
        print(i)
        subRecursive(i)
        recursive(i-3)
    else :
        return

recursive(10)