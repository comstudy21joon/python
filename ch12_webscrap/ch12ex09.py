#findall() 메소드 : 정규식 패턴과 매칭되는 데이터를 리스트로 반환.
import re
# 정규식 패턴을 그룹핑 한다
regex = re.compile(r'([\d]{2,3})-(\d\d\d\d-\d\d\d\d)')
txt = 'cell phone: 010-1234-5678, office phone: 02-1234-5678'
dataList = regex.findall(txt)

print(dataList)