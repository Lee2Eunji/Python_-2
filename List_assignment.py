List = []
for x in range(1, 16):
    num = int(x)
    List.append(num)
if range == 14:
    print(List)

i = 1
while i <= 7:
    print(i * 2)
    i = i + 1
    if i == i * 2:
        del(List[i])
if i == i * 3:
    del(List[i])

print(List.pop(1))
List.insert(1, 2)
List.insert("3")
List.sort()