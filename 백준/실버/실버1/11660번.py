'''import sys
n, m = map(int, sys.stdin.readline().split())
mlist = [[] for _ in range(n)]
for i in range(n):
    mlist[i] = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sum=0
    for i in range(x1-1, x2):
        for k in range(y1-1, y2):
            sum += mlist[i][k]
    print(sum)
#시간 초과
'''
import sys
n, m = map(int, sys.stdin.readline().split())
alist = [[] for _ in range(n)]
blist = [[0]*(n+1) for _ in range(n+1)] #n+1크기의 2차원 배열 선언

for i in range(n):
    alist[i] = list(map(int, sys.stdin.readline().split()))

#구간합 배열 계산
for i in range(1, n+1):
    for k in range(1, n+1):
        blist[i][k] = blist[i-1][k] + blist[i][k-1] - blist[i-1][k-1] + alist[i-1][k-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sum = blist[x2][y2] - blist[x1-1][y2] - blist[x2][y1-1] + blist[x1-1][y1-1]
    print(sum)

#실버 1, 성공