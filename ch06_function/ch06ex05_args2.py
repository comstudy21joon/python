
# 리스트를 가변적으로 받아서 처리하는 함수
# 리스트의 세로 합계를 만들어 주는 함수
def mkVerticalTotal(*scoreList) :
    totalList = []
    for list in scoreList :
        for i, score in enumerate(list) :
            try :
                totalList[i] += score
            except :
                totalList.append(score)

    return totalList


totalList = mkVerticalTotal([60,60,60],[90,90,90],[30,30,30,100])
print(totalList)
