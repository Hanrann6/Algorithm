#26069번 - 실버 4
n = int(input())
people = []
people.append("ChongChong")
for _ in range(n):
    a, b = input().split()
    if a in people and b in people:
        continue
    elif a in people:
        people.append(b)
    elif b in people:
        people.append(a)

print(len(people))