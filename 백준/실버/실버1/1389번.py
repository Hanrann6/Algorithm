import sys
input = sys.stdin.readline
MAX = sys.maxsize
n, m = map(int, input().split()) # 유저 수, 관계 수
d = [[MAX for i in range(n+1)] for _ in range(n+1)] # 최단 거리

# 자기 자신은 0
for i in range(1, n+1):
    d[i][i] = 0

# 거리 저장
for _ in range(m):
    a, b = map(int, input().split())
    d[a][b] = 1
    d[b][a] = 1 # 양방향 관계

# 플로이드 워셜
for i in range(1, n+1): # 경유지 i
    for j in range(1, n+1): # 출발 노드 j
        for k in range(1, n+1): # 도착 노드 k
            if d[j][k] > d[j][i] + d[i][k]: # 경유지 찍은 게 더 짧으면
                d[j][k] = d[j][i] + d[i][k]

bacon = []
for friend in d:
    bacon.append(sum(friend))

print(bacon.index(min(bacon)))