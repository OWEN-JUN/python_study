# list 연산

#리스트 덧셈

color1 = ['빨강', '파랑', '녹색' ]
color2 = ['오렌지', '검정', '흰색']

color3 = color1 + color2

print(color3)



#list 추가, 삭제
#append(), extend(), insert(), remove()
#append() : 새로운 값을 기존 리스트의 맨 끝에 추가
heros = ['캡틴마블', '아이언맨', '헐크']
print(heros)

heros.append('토르')
print(heros)

#extend() : 리스트 확장(새로운 리스트를 기존 리스트에 추가)
heros1 = ['캡틴아메리카', '블랙쉐도우', '로키']
ex = ['슈퍼맨', '스파이더맨']
#heros1.extend(['슈퍼맨', '스파이더맨'])
heros1.extend(ex)

print(heros1)

#insert() : 기존 리스트에 추가를 함, 중간 삽입이 가능

colors = ['주황색', '노랑색', '초록색', '파랑색']
colors.insert(0, '빨간색')
print(colors)

#remove() : 리스트 내의 특정 요소값을 삭제
print(heros1)

heros1.remove('슈퍼맨')

print(heros1)

search = "로키" in heros1
print(search)