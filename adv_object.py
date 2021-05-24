# 글로벌 변수 선언
global_a = 1
global_b = "GLOBAL SCOPE"

# 사용자 정의 함수
def func():
    # 로컬 변수 선언
    local_a =2
    local_b = "LOCAL SCOPE"

# 사용자 정의 객체
class MyClass:

# 심볼 테이블 확인
    def symbol_table():
    # 글로벌 심볼 테이블 확인
    print(globals())
    print(type(globals()))
    # 심볼테이블은 객체의 심볼, 객체의 id룰 담고 있는 dict
    print("global_a:", globals().get("global_a"))
    print("global_b:", globals().get("global_b"))

    func()

    # 객체 내부의 __dict__ 속성을 확인하면 객체 내부의 심볼 테이블을 확인 가능
    # 1. 정의된 함수 객체 내부의 심볼 테이블 확인
    func.dynamic = "Hello"
    print(func.__dict__)

    # 2. 클래스 객체 내부의 심볼 테이블 확인
    print(MyClass.__dict__) # 사용자 정의 클래스
    print(int.__dict__) # 내장 정의 클래스의 심볼 테이블


def ref_count():
    """
    참조 카운트 예제
    """
    x = object()
    print(x, type(x))

    # 참조 카운트 확인
    import sys # 시스템 모듈 임포트
    print("REFCOUNT:", sys.getrefcount(x))

    y=x # y에 x의 참조 주소를 복사
    print("REFCOUNT:", sys.getrefcount(x))

    # x의 참조를 삭제
    del x
    print("REFCOUNT:", sys.getrefcount(y))

    # 참조 카운트가 0인 객체 발견 -> garbage Collection 작업을 수행

def objec_id():
    """
    객체 ID에 관한 예쩨 : 객체 ID는 객체의 참조 주소
    """
    # 불변 자료형 : 두값이 같으면 같은 객체
    i1 = 10
    12 = int(10)
    print("int:", hex(id(11), hex(id(12))))

    # 가변 자료형 : 값이 같아도 별개의 객체
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print("list:", hex(id(lst1), hex(id(lst2))))

    lst3 = lst2 # 팜조 복사 : 객체 주소의 복사
    print("참조 복사", hex(id(lst2)), hex(id(lst3)))

    # == 은 동등성의 비교 (값이 같으니), is는 동일성(같은 객체냐)의 비교
    print("불변객체의 비교:", i1==i2, i1 is i2) # 값은 같고(동등), 객체도 같다(동일)
    print("불변객체의 비교:", lst1 == lst2, lst1 is lst2) # 같은 값고, 객체는 다르다

if __name__=="__main__":
    symbol_table()
    ref_count()
    object_id()