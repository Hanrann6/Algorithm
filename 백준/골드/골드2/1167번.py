import sys
from collections import deque
V = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    info = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(info) - 1, 2): #인덱스별 간선 저장
        graph[info[0]].append([info[i], info[i + 1]])

visited = [False] * (V + 1) #방문 여부
distance = [0] * (V + 1) #거리


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while (queue):
        new = queue.popleft()
        for i in graph[new]: #연결된 모든 노드 확인
            if (not visited[i[0]]):
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[new] + i[1] #거리 업데이트


BFS(1)
index = distance.index(max(distance)) #가장 먼 노드의 인덱스

visited = [False] * (V + 1)
distance = [0] * (V + 1)

BFS(index) #새 시작점으로 dfs 재실행
print(max(distance))