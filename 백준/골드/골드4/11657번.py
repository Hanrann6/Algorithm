import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 도시 수, 노선 수
edge = []
distance = [sys.maxsize] * (n+1) # 거리

for i in range(m):
    a, b, c = map(int, input().split())
    edge.append((a, b, c)) # 출발, 도착, 가중치

# 벨만-포드
distance[1] = 0
for i in range(n-1):
    for start, end, dis in edge:
        if distance[start] >= sys.maxsize:
            continue
        if distance[start] + dis < distance[end]:
            distance[end] = distance[start] + dis

# 음수 사이클 존재하는지 테스트
change = False
for start, end, dis in edge:
    if distance[start] >= sys.maxsize:
        continue
    if distance[start] + dis < distance[end]:
        change = True # 바뀜

if change:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] >= sys.maxsize:
            print(-1)
        else:
            print(distance[i])