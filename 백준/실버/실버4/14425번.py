import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [input() for _ in range(n)]
m = [input() for _ in range(m)]

ans = 0
for mm in m:
    if mm in s:
        ans += 1

print(ans)
