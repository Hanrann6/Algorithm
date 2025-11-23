import sys
input = sys.stdin.readline
n = int(input())
a = [[] for _ in range(n)]
visited = [False] * n
d = [0] * n
lcm=1

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def dfs(v):
    visited[v] = True
    for i in a[v]:
        next = i[0]
        if not visited[next]:
            d[next] = d[v] * i[2] // i[1]
            dfs(next)

for i in range(n-1):
    c, b, p, q = map(int, input().split())
    a[c].append((b, p, q))
    a[b].append((c, q, p))
    lcm *= (p * q // gcd(p, q))

d[0] = lcm
dfs(0)
mgcd = d[0]

for i in range(1, n):
    mgcd = gcd(mgcd, d[i])

for i in range(n):
    print(int(d[i] // mgcd), end=' ')

# 책 베낌 골드2