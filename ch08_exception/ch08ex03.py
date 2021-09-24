
try:
    message = user + "님 안녕하세요^^"
    print(message)
except NameError as e:
    print("식별자가 정의 되지 않았습니다!")
    print(e)