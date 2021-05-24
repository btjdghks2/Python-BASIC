# 함수 스코핑 룰
x = 1 # Global

def scope_func(a):
    return  a + x   # local 스코프에 x가 없음 -> 글로벌 x를 참조

def scope_func2(a):
    x = 2   # 치환 -> 로컬 스코프에 x 심볼이 생성 -> 글로벌 x가 아니다
    return  a + x   # local 스코프 a, local Scope x 합산 리턴

print(scope_func(10))
print(scope_func2(10))
print("global x:", x) # scop_fun2에서 x가 치환되었지만 global x는 변경되지 않음