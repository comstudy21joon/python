import re

regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
txt = 'phone number : 010-1234-5678'
data = regex.search(txt)
data2 = regex.match(txt[15:28])

print(data)
print(data.span())
print(data2)