# fp = open("io_test.txt", "w", encoding='utf-8')
# fp.write("파일 입출력 테스트 2번째")
# fp.close()

with open("io_test.txt","w", encoding='utf-8') as fp :
	fp.write("with문을 이용한 파일 입출력 테스트")