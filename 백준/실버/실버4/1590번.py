#1590번 - 실버 4
import sys
n, t = map(int, sys.stdin.readline().split())
start = []
inter = []
count = []
for i in range(n):
    s, i, c = map(int, sys.stdin.readline().split())
    start.append(s)
    inter.append(i)
    count.append(c)

wait = []
for i in range(n):
    if(t > start[i] + inter[i]*(count[i]-1)):
        continue
    for _ in range(count[i]):
        if(t <= start[i]):
            wait.append(start[i] - t)
            break
        start[i] += inter[i]
if not wait: #리스트가 비어 있는 경우 not 사용
    print(-1)
else:
    print(min(wait))