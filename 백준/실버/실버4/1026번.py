#1026번 - 실버 4
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
s = 0
a.sort()
a.reverse()
b.sort()
for i in range(n):
    s = s + a[i]*b[i]
print(s)