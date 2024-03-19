foods = ['햄버거','치킨','족발']

print(id(foods))
print(hex(id(foods))) # 16진수

mv = memoryview(b'happy day') # b 접두사는 문자열을 바이트로 처리하겠다는 뜻

print(mv)

print(mv[0]) # 바이트 형태기 떄문에 유니코드로 출력이 된다.
print(mv[1])
print(mv[2])
print(mv[3]) # 2,3 인덱스는 둘다 p이기 떄문에 같다. 덱스?



