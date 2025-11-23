import sys
import heapq
input = sys.stdin.readline
v, e = map(int, input().split()) # 노드 수, 간선 수
start = int(input()) # 출발 노드
graph = [[] for _ in range(v+1)]
distance = [sys.maxsize] * (v+1) # 최단 거리

# 연결 리스트
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:  # 이미 짧으면 continue
            continue

        for node in graph[now]:
            if dis + node[1] < distance[node[0]]:  # 현재 거리가 더 짧으면
                distance[node[0]] = dis + node[1]
                heapq.heappush(q, (dis + node[1], node[0]))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == sys.maxsize:
        print("INF")
        continue
    print(distance[i])