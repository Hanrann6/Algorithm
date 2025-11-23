#10811번 - 브론즈 2
n, m = map(int, input().split()) #list의 길이
list = []
for i in range(n):
    list.append(i+1)

for _ in range(m):
    i, j = map(int, input().split())
    list2 = list[i-1:j]
    list2.reverse() # 뒤집기
    list[i-1:j] = list2

print(*list) #언패킹해서 출력