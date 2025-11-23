import sys
input = sys.stdin.readline

n = int(input())
dot = []
for _ in range(n):
    x, y = map(int, input().split())
    dot.append((x, y))
dot.append(dot[0])

ans = 0
for i in range(0, n):
    ans += dot[i][0]*dot[i+1][1] - dot[i+1][0]*dot[i][1]

print(round(abs(ans/2), 1))