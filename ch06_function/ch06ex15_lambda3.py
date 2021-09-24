# 람다표현식으로 사용
fruits = ['갑오징어','꼴두기','복','명태','바다거북이']
fruits.sort(key = lambda  x:len(x))
print("fruits => ", fruits)