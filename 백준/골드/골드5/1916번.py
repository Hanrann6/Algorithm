import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
distance = [sys.maxsize] * (n+1)

for _ in range(m): # 그래프 생성
    a, b, c = map(int, input().split())
    bus[a].append((b, c))

def dijkstra(start, end):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue

        for node in bus[now]:
            if dis + node[1] < distance[node[0]]:
                distance[node[0]] = dis + node[1]
                heapq.heappush(q, (dis + node[1], node[0]))

    return distance[end]

start, end = map(int, input().split())
print(dijkstra(start, end))