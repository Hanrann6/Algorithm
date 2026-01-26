import sys
input = sys.stdin.readline

n, k = map(int, input().split())
circle = [i for i in range(1, n+1)]

ans = []
idx = k-1
# 3, 6,
while len(circle) != 0:
    idx %= len(circle)
    ans.append(circle[idx])
    del circle[idx]
    idx += (k-1)

print('<', end='')
for i in range(n-1):
    print(ans[i], end=', ')
print(ans[n-1], end=">")
# print문에서 쉼표로 붙이면 사이에 공백 들어감!