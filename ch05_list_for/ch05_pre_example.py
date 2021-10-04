# set 구조를 이용한 로또번호 검색기
# Step 01
# import random
#
# # 1~2사이의 난수 값을 무작위로 발생 시킨다.
# # 1과 2포함
# # 첫번째 난수 발생 및 확인
# num = random.randint(1,2)
# print('num :', num)
# # 두번째 난수 발생 및 확인
# num = random.randint(1,2)
# print('num :', num)
# # 세번째 난수 발쌩 및 확인
# num = random.randint(1,2)
# print('num :', num)







# set 구조를 이용한 로또번호 검색기
# Step 02
# import random
#
# lotto = set()
# print('type :', type(lotto))
#
# lotto.add(1);
# lotto.add(1);
# lotto.add(2);
# lotto.add(2);
# lotto.add(2);
# lotto.add(3);
# lotto.add(3);
# print(len(lotto) )
#
# for i in lotto :
#     print(i, end="    ")








# # set 구조를 이용한 로또번호 검색기
# # Step 03
import random

lotto = set()

while len(lotto) < 6 :
    lotto.add(random.randint(1,45))

print("--- 로또번호 생성 ---")
for i in lotto :
    print(i, end="    ")
