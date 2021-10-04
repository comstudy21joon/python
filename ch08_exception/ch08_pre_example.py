import logging
from time import sleep

while True :
    try :
        age = int(input("나이 입력 >>"))
        print('입력 한 나이는 ', age)
        break
    except  ValueError as e  :
        logging.warning("나이는 정수로 입력 하세요!");
        sleep(0.5)
        continue

print("The End!")