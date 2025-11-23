import sys
input = sys.stdin.readline

n = int(input())

def bunhe(n):
    ns = str(n)
    l = len(ns)
    ns = map(int, ns)
    return sum(ns)

ans = 0
for i in range(1, n):
    if i + bunhe(i) == n:
        ans = i
        break

print(ans)