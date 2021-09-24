'''
import random

min = 1
max = 100
cnt = 5
sysNum = random.randint(min, max)
print('시스템이 선택한 하나의 정수를 맟춰보세요. 힌트:({})'.format(sysNum))

while cnt > 0 :
    print('기회는 {}회 남았습니다.'.format(cnt))
    userNum = int(input('입력({}~{}사이)>> '.format(min, max)) )
    if userNum == sysNum :
        print('빙고! 정답입니다^^')
        break
    if userNum > sysNum :
        print('너무 큰 숫자를 입력 했습니다!')
        max = userNum - 1
    else :
        print('너무 작은 숫자를 입력 했습니다.')
        min = userNum + 1

    cnt -= 1


if cnt <= 0 :
    print('실격! 기회를 모두 소진 하였습니다.')
'''


'''
users = {'철수': "태극기",'영희': ""}

keys = list(users.keys());
cnt = 0;
word = ""
print("첫번째 제시어는 "+users['철수']+"입니다.")
while True :
    prevUser = keys[cnt%2] #이전 사용자
    curUser = keys[(cnt+1)%2] #현재 사용자
    
    word = input(curUser + "입력>> ")
    prevWord = users[prevUser] # 이전 사용자 단어
    if prevWord[len(prevWord)-1] != word[0] :
        print("실격!", prevUser, "승리!")
        break

    cnt += 1
    users[curUser] = word #현재 사용자의 단어 저장
'''





'''
def concatLIst(lis1, lis2) :
    newList = []
    for w in lis1 :
        newList.append(w)
    for w in lis2 :
        newList.append(w)

    return newList


lis1 = [100, 200, 300, 400]
lis2 = [500, 600, 700]
lis = concatLIst(lis1, lis2)
print(lis)
'''



'''
def removeElement(lis, value) :
    i = 0
    size = len(lis)
    while i < size :
        try :
            lis.remove(value)
            size = len(lis)
        except :
            pass
        i += 1


lis = ['오징어', '꼴뚜기', '대구', '오징어', '명태', '거북이', '고래']
removeElement(lis, '오징어')

print(lis)
'''



print("단어를 입력 하시오(종료는 그만을 입력하시오) ")
wordList = []
while True :
    word = input("단어 입력>> ")
    if word == "그만" :
        break

    wordList.append(word)


search = input("개수를 알고자 하는 단어 입력>> ")
cnt = 0;
for w in wordList :
    if w == search :
        cnt += 1

print(wordList)
print('리스트에서 ', search, '는', cnt, '개입니다.')
