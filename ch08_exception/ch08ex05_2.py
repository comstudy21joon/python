
user_name = input("성명 입력 : ")

try :
    assert len(user_name) >= 3, "성명은 3글자 이상이어야 합니다."
    print("user_name =>", user_name)
except AssertionError as e :
    print(e)
