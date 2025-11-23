import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split()) # 정점 수, 간선 수
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 양방향 그래프
    graph[b].append((a, c))

def dijkstra(start, end):
    distance = [sys.maxsize] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue

        for node in graph[now]:
            if dis + node[1] < distance[node[0]]:
                distance[node[0]] = dis + node[1]
                heapq.heappush(q, (dis + node[1], node[0]))

    return distance[end]

v1, v2 = map(int, input().split()) # 지나야 하는 경로
ans1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
ans2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
ans = min(ans1, ans2)

if ans >= sys.maxsize:
    print(-1)
else:
    print(ans)