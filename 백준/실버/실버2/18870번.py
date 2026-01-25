import sys
input = sys.stdin.readline

n = int(input())
l1 = list(map(int, input().split())) # 원본
d = dict()
i = 0
k = min(l1)
for l in sorted(l1): # 0으로 초기화
    if (k < l):
        i += 1
    d[l] = i
    k = l

ans = []
for l in l1:
    ans.append(d[l])

print(*ans)