import sys
input = sys.stdin.readline
MAX = sys.maxsize
n = int(input()) # 노드 개수
d = [[MAX for i in range(n+1)] for _ in range(n+1)] # 최단 거리

# 거리 저장
for i in range(n):
    edge = list(map(int, input().split()))
    for k in range(n):
        if edge[k] == 1:
            d[i+1][k+1] = 1

# 플로이드 워셜
for i in range(1, n+1): # 경유지 i
    for j in range(1, n+1): # 출발 노드 j
        for k in range(1, n+1): # 도착 노드 k
            if d[j][k] > d[j][i] + d[i][k]: # 경유지 찍은 게 더 짧으면
                d[j][k] = d[j][i] + d[i][k]

for i in range(1, n+1):
    for k in range(1, n+1):
        if d[i][k] == MAX: # 경로 없음
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()