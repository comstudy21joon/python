# Set 구조 선언
s = {"사과","오랜지","딸기","바나나","오랜지"}
print(type(s))
print(len(s))
print(s)
s.clear()
print("모든 항목 제거 후:", len(s))
print("모든 항목 제거 후:", s)
# 새로운 빈 셋 구조 선언
s2 = set()
# 셋에는 값이 중복되게 담기지 않는다.
s2.add(100)
s2.add(200)
s2.add(200)
s2.add(100)
print(type(s2))
print(s2)
s2.remove(200)
#s2.remove(1000)
s2.discard(1000)
print(s2)
# 문자열의 요소를 Set형식으로 변환하기(문자 중복 제거)
s3 = set("aaabbbccceee1223fff")
print(len(s3));
print(s3)