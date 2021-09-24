'''
d = dict()

print(type(d))

#d.put('no', '10')
d['no'] = '10'
no = d.get('no')
no2 = d['no']

print(no)
print(no2)
'''
import random
from pprint import pprint

'''
positive = []
negative = []

for i in range(10) :
    num = int(input('입력{}>> '.format(i+1)))
    if num > 0 :
        positive.append(num)
    else :
        negative.append(num)

print("양수 리스트 >> ", positive)
print("음수 리스트 >> ", negative)
'''

'''
lis = [10,20,30,40,50,60,70,80.90,100]
total = 0

print(lis)

for i in range(3) :
    num = int(random.choice(lis))
    print(num ,  end=' ')
    total += num

print('=', total)
'''

# random.choice([1,2,3])



'''
lis = list(range(1,17))
random.shuffle(lis)
#print( lis )

#lis = [[],[],[],[]]
new_lis = []
cnt = 0
for i in range(4) :
    new_lis.append([])
    for j in range(4) :
        new_lis[i].append(lis[cnt])
        cnt  += 1

pprint(new_lis, indent=2, width=20)
'''

'''
lotto = {0,}
print(type(lotto))
lotto.add(10)
print(lotto)
'''

'''
print("로또 번호를 생성 합니다.")
lotto = set()
#print(type(lotto))
while len(lotto) < 6 :
    lotto.add(random.randint(1,46))

print(lotto)
'''



person = {}

for key in ['no', 'name', 'phone', 'email'] :
    data = input(key+" 입력>> ")
    person[key] = data

pprint(person, indent=4, width=20)
keys = person.keys()
values = person.values();
print(keys)
print(values)

