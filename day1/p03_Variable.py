#주석문..코드상의 결과에 영항을 미치지 않음
#그 코드의 설명을 적는다
def typecheck(val):
    print(type(val))

p = 0 #p 정수변수
s = "i love you" #s는 문자열 변수
w = 2.5 #w는 실수 변수
d = True #d는 부울 변수(True, False)


print(p)
print(s)
print(w)
print(d)
result = type(p)

print(type(p), type(s), type(w), type(d))
typecheck(p)
typecheck(s)
typecheck(w)
typecheck(d)
typecheck(result)
