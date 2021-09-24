class UserDefinitionError(Exception):
	def __init__(self, message):
	    super().__init__("사용자 정의 예외: "+message)


import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s - %(message)s')


try:
    message = "안녕하세요^^"
    print(user + message)
    logging.debug(message)
except NameError as e:
    logging.debug("식별자가 정의 되지 않았습니다!")

    try:
        raise UserDefinitionError(str(e))
    except UserDefinitionError as user_e:
        logging.debug(user_e)