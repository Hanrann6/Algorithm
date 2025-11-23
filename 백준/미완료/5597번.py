#5597번

list = list(range(1, 31))
for i in range(28):
    n = int(input())
    list.remove(n)

print(list[0])
print(list[1])