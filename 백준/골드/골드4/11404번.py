import sys
input = sys.stdin.readline
MAX = sys.maxsize
n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
d = [[MAX for i in range(n+1)] for _ in range(n+1)] # 최단 거리

# 자기 자신은 거리 0
for i in range(1, n+1):
    d[i][i] = 0

# 거리 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    if d[a][b] > c:
        d[a][b] = c


# 플로이드 워셜
for i in range(1, n+1): # 경유지 i
    for j in range(1, n+1): # 출발 노드 j
        for k in range(1, n+1): # 도착 노드 k
            if d[j][k] > d[j][i] + d[i][k]: # 경유지 찍은 게 더 짧으면
                d[j][k] = d[j][i] + d[i][k]


for i in range(1, n+1):
    for k in range(1, n+1):
        if d[i][k] == MAX:
            print(0, end=' ')
        else:
            print(d[i][k], end=' ')
    print()