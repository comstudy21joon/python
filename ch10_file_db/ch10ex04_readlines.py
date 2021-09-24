fp = open("io_test.txt","r", encoding='utf-8')
lines = fp.readlines()

for line in lines :
	print(line, end="")

fp.close()
print("-"*30)