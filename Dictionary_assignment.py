Dic = {}
x = int
while x:
    Dic.get(int(input("정수를 입력해 주세요.: ")))
    if Dic == 0:
        print("그만")
        print(Dic)
        break
    Dic.get(str(input("문자를 입력해 주세요.: ")))
    if Dic == "문자열 종료":
        print("그만")
        print(Dic)
    break

print(list(Dic.keys()))
print(list(Dic.values()))
print(list(Dic.items()))