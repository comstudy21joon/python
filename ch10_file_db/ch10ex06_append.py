fp = open("io_test.txt", "a", encoding='utf-8')
for i in range(5,8) :
	data = "{0}번째 라인 ...\n".format(i)
	fp.write(data)
fp.close()

fp = open("io_test.txt","r", encoding='utf-8')
data = fp.read()
print(data, end="")
fp.close()