class UserDefinitionError(Exception):
	def __init__(self, message):
	    super().__init__("사용자 정의 예외: "+message)


try:
    message = user + "님 안녕하세요^^"
    print(message)
except NameError as e:
    print("식별자가 정의 되지 않았습니다!")

    try:
        raise UserDefinitionError(str(e))
    except UserDefinitionError as user_e:
        print(user_e)