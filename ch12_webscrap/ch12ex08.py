import re
# 정규식 패턴을 그룹핑 한다
regex = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')
txt = 'phone number : 010-1234-5678'
data = regex.search(txt)
# 그룹핑 된 데이터 확인
print(data.group(1))
print(data.group(2))
print(data.group(0))
# groups()는 그룹을 튜플로 반환
print(data.groups())
# 튜플 언팩킹
a, b = data.groups()
print(a, b)