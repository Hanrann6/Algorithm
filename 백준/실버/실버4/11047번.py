import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

money.reverse() #내림차순으로 정렬
cnt = 0
for m in money:
    if m <= k:
        d = k // m
        cnt += d
        k -= (d * m)

print(cnt)