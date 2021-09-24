'''
print()
input()
abs()
all()
any()
chr()
enumerate()
eval()
filter()
hex()
isinstance()
lambda
len()
list()
map()
max()
min()
open()
ord()
pow()
range()
sorted()
str()
.upper()
.lower()

https://docs.python.org/3/library/functions.html
'''

# filter 내장 함수는 두번째 인자로 주어진 iterable에서
# 조건에 맞지 않는 항목을 제거 할 수 있습니다.
# 아래의 코드는 lis 리스트에서 10의 배수가 아닌 항목을 제외하고
# 새로운 리스트를 생성 해줍니다.

def choose(a) :
    if(a%10 == 0) :
        return a


lis = [10,25,30,46,50]

lis2 = list(filter(choose, lis) )

print(lis2)




