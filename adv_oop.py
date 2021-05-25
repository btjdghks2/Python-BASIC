class MyString(str):    # str 클래스를 상속 받은 MyString
    pass    # MyString은str 클래스에서 모든 멤버들을 물려 받는다

s= MyString()   # 인스턴스 생성
print(type(s))  # 타입의 확인
print(MyString.__bases__)   #기반 클래스의 확인
print(str.__bases__)    # 모든 클래스의 최상위 클래스는 object

# 파이썬은 다중 상속이 가능
class mybj:
    pass

class Chimera(str, mybj):
    pass

print(type(Chimera))
print(Chimera.__bases__)

# 하위 클래스 or 파생 클래스 : issubclass 함수
print("Chimera는 str의 서브클래스?", issubclass(Chimera, str))
print("Chimera는 mybj의 서브 클래스?", issubclass(Chimera,mybj))

# 상위 클랴스 or 기반 클래스: 별도 함수 없음, __bases__ 사용
# MyString은 str을 상속 -> str의 모든 멤버를 상속
ms = MyString("Python")
print(ms)
print(dir(ms))
# str의 모든 메서드를 그대로 활용
print(ms.upper())

# 클래스 생성
