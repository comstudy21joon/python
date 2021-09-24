fp = open("io_test.txt", "r", encoding='utf-8')
while True:
	data = fp.readline()
	data = data[0:len(data)-1] # 마지막에 '\n'문자를 제거한다.
	if not data :
		break;
	print(data)
fp.close()