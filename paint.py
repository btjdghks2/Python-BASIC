# Text
from point import Point

def bound_class_method():
    # 직접 인스턴스 명시 -> 멤버에 접근
    p = Point() #생성
    p.setX(10)
    p.setY(20)
    print(p.getX(), p.getY(), sep=",")
    print(p.getX, p.getY)
    # get X, getY가 bound method로 샐행됨을 확인


def unbound_class_method():
    # 클래스에 인스터스를 전달해서 인스턴스 내부의 메서드 호출
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 20)
    print(Point(p), Point.getY(p))
    print(Point.getX,Point.getY)
    # Point class 내의 함수

def class_mamber_test():
    p1 = Point()
    p1.setX(10)
    p1.setY(20)

    print("p1:{},{}".format(p1.getX(),p1.getY()))
    print("instance_count:",
          p1.isinstance_count,  # 인스턴스에서 접근 가능
          Point.isinstance_count)   # 인스턴스 없이도 접근 가능

def test_lifecycle():
    p1 = Point(10, 20) # 생성자 사용
    print("instance count:", Point.instance_count)

    p2 = Point() # 기본 값 사용
    print("instance count:", Point.instance_count)

    print(p1, p2)

 def test_print():
     p1 = Point(10,10)
     print("p1:", p1)   # __str__ 호풀
     print("p1:",p1)

    # __str__ 일반 사용자가 보기 쉽게 출력하는 포멧
    # __repr__은 개발자가 객체 복원하기 위해 출력하는 포멧

    print(repr(p1)) # __repr__ 호출
    p2 = eva;(repr(p1)) # __repr__ cnffurvhaptdmfh rorcp qhrdnjs
    print("p2:", p2, type(p2))

    # __ str__ 비공식적 문자열(일반사용자용)
    #__repr__ 공식적 문자열(개발자용)

# 역이행 연산자 +
def __radd__(self, other):  # other + Point
    if isinstance(other, int):
        self.x += other
        self.y += other

    return self


# - 연산자 오버로딩
def __sub__(self, other):
    if isinstance(other, Point):
        self.x -= other.x
        self.y -= other.y
    elif isinstance(other, int):
        self.x -= other
        self.y -= other

    return self


# == 오버로딩
def __eq__(self, other):
    return self.x == other.x and self.y == other.y
if __name__ =="__main__":
    bound_class_method()
    unbound_class_method()
    class_mamber_test()
    test_lifecycle()
    test_print()