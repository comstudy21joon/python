'''
name = input("이름 입력>> ")
while True :
    try :
        age = int(input("나이 입력>> "))
        break
    except :
        print("ValueError가 발생 했습니다. 나이를 다이 입력하세요.")
        continue

print(name + "님은 ", end="")
if age < 19 :
    print("미성년자입니다")
elif age < 35 :
    print("청년입니다.")
elif age < 65 :
    print("중년입니다.")
else :
    print("노년입니다.")
'''

'''
import time


fish_list = ['오징어','꼴뚜기','대구','명태','거북이']
print("생선을 주문하세요!")
for i, fish in enumerate(fish_list) :
    print("(%d)%s " %(i+1,fish), end=" ")

while True :
    try :
        choice = int(input(">> "))
        print("-" * 55)
        print(fish_list[choice - 1], end=" ")
        break
    except IndexError as e :
        print("IndexError가 발생 했습니다.")
        print("다시 선택", end=" ")
    except ValueError as e :
        print("ValueError가 발생 했습니다.")
        print("다시 선택", end=" ")

print("정상 주문 완료!")
'''

'''
fish_list = ['오징어','꼴뚜기','대구','명태','거북이']
print("생선을 주문하세요!")
for i, fish in enumerate(fish_list) :
    print("(%d)%s " %(i+1,fish), end=" ")

while True :
    try :
        choice = int(input(">> "))
        print("-" * 55)
        if choice <= 0 :
            raise Exception('알 수 없는 에러입니다!')
        print(fish_list[choice - 1], end=" ")
        break
    except IndexError as e :
        print("IndexError가 발생 했습니다.")
        print("다시 선택", end=" ")
    except ValueError as e :
        print("ValueError가 발생 했습니다.")
        print("다시 선택", end=" ")
    except Exception as e :
        print("알 수 없는 예외가 발생 했습니다.")
        print("다시 선택", end=" ")

print("정상 주문 완료!")
'''


"""
import logging

fish_list = ['오징어','꼴뚜기','대구','명태','거북이']
print("생선을 주문하세요!")
for i, fish in enumerate(fish_list) :
    print("(%d)%s " %(i+1,fish), end=" ")

while True :
    try :
        choice = int(input(">> "))
        print("-" * 55)
        if choice <= 0 :
            raise Exception('알 수 없는 에러입니다!')
        print(fish_list[choice - 1], end=" ")
        break
    except IndexError as e :
        logging.error("IndexError 발생")
    except ValueError as e :
        logging.error("ValueError 발생")
    except Exception as e :
        logging.error("알 수 없는 예외가 발생")

    time.sleep(0.1)
    print("다시 선택", end=" ")

print("정상 주문 완료!")
"""

import logging
import time

root_logger= logging.getLogger()
handler = logging.FileHandler('log_fish_order.txt', 'w', 'utf-8')
handler.setFormatter(logging.Formatter('%(name)s - %(asctime)s - %(message)s'))
root_logger.addHandler(handler)

fish_list = ['오징어','꼴뚜기','대구','명태','거북이']
print("생선을 주문하세요!")
for i, fish in enumerate(fish_list) :
    print("(%d)%s " %(i+1,fish), end=" ")

while True :
    try :
        choice = int(input(">> "))
        print("-" * 55)
        if choice <= 0 :
            raise Exception('알 수 없는 에러입니다!')
        print(fish_list[choice - 1], end=" ")
        break
    except IndexError as e :
        print("IndexError 발생")
        root_logger.error("IndexError 발생")
    except ValueError as e :
        print("ValueError 발생")
        root_logger.error("ValueError 발생")
    except Exception as e :
        print("알 수 없는 예외가 발생")
        root_logger.error("알 수 없는 예외가 발생")

    time.sleep(0.1)
    print("다시 선택", end=" ")

print("정상 주문 완료!")