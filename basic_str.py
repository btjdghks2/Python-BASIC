def define_str(): # 문자열의 정의
    # 한 줄 문자열의 정의
    s1 = "Hello Python" # 쌍따옴표("), 홀따옴표(') 모두 가능
    s2 = str("Hello Python") # xkdlq gkatn dldyd todtjd
    s3 = str(3.14159) # 타 타임을 문자열로 변환

    print(s1, s2, s3)
    print(type(s1),type(s2),type(s3))

    print("s1은 str의 객체?", isinstance((s1,str)))

    # 여러 줄 문자열의 정의
    # 쌍따옴표 세 개("""), 홀따옴표 세개(''')
    s4 = """ Life is too short, you need Python
파이썬은 데어터 처리가 중요한 시대에서
가장 널리 사용되는 언어이다.
    
    """
    print(s4)

    # 여러줄 문자열은 한 줄 주석만 있는 파이썬에서
    # 여러줄 주석을 사용할 경우에도 사용
    # 메서드 정의부 바로 아래 여러 줄 문자열을 입력하면
    # help 명령어를 이용해서 해당 메서드의 주석을 볼수 있다.


def string_oper(): # 문자열 연산
    """
    문자열연산 연습
        str : len -> 길이 확인
        연결(+), 반복(*) 포함여부 확인 가능
        인덱싱, 슬라이싱 가능
        ㅑimmutable -> 내부 데이터 변경 불가
    """
    str = "First String"
    str1 = "Python"
    str2 = "Second String"

    # 길이 : len
    print("str1 length", len(str1))

    # 변경 불가 자료형
    # str[0] = 'f' -> error

    # 인덱싱 : 배열과 비슷하게 인덱스로 접근
    print("정인덱싱:", str1[0], str1[1], str1[2], str1[3], str1[4],str1[5])
    print("역인덱싱:", str1[-6], str1[-5], str1[-4], str1[-3], str1[-2],str1[-1])

    # 슬라이싱 : 경계 범위 설정에 유의
    print("[2:4]슬라이싱:", str1[2:4]) # [시작경계 : 끝경계]
    print("[-4:-2] 슬라이싱:", str1[-4:-2]) # 역인덱스를 이용한 슬라이싱
    print("[0:3] 슬라이싱 :", str1[0:3])
    print("[:3] 슬라이싱:", str1[:3]) # 시작경계를 생략 -> 처음부터
    print("[d:len(str1)] 슬라이싱:", str1[3:len(str1)])
    print("[3:] 슬라이싱", str1[3:]) # 끝경계를 생략





if __name__ == "__main__":
    #define_str()
    string_oper()