#### 클래스 만들기
# 1. class 키워드를 이용해서 클래스를 선언한다. 내용이 없을 경우 pass만을 적는다.
# 2. 클래스 내부에 생성자를 선언한다.
# 3. __init__() 생성자에서 필드를 초기화 한다.
# 4. 클래스 내부에 메소드를 선언한다. 내용이 없을 경우 pass만을 적는다.
# 5. 메소드에서 필드 값을 사용한다.
# 6. __str__() to string 메소드를 선언한다.
# 7. __str__() 메소드에서 필드값을 return한다.
# 8. 클래스 외부에서 객체를 생성하고 사용한다. 참조변수 = 클래스()
#
# - self 변수는 객체 자신을 가리키는 참조 변수이다.
# - self는 클래스 내부에서만 호출 하고 외부에서는 호출 할 수 없다.
import math

class Circle :
    #pass
    def __init__(self, r):
        #pass
        self.r = r
        self.mkArea()
        self.mkLine()

    def mkArea(self):
        self.area = math.pi * self.r**2

    def mkLine(self):
        self.line = 2 * math.pi * self.r

    def __str__(self):
        return "area:%.3f, line:%.3f" %(self.area,self.line)


circle = Circle(10)
print(circle)