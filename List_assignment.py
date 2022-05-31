List = []

for x in range(0, 15):
    num = int(input("숫자를 입력하세요.: "))
    List.append(num)
    if(x == 14):
        print(List)

for x in List:
    if(x % 2 == 0):
        List.remove(x)
print(List)

for x in List:
    if(x % 3 == 0):
        List.remove(x)
print(List)

List.pop(0)
print(List)
List.insert(0, 2)
List.insert(1, 3)
print(List)