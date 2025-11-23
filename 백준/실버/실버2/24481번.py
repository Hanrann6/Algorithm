import sys
sys.setrecursionlimit(10**6) #10**5로는 런타임 에러 남.
input = sys.stdin.readline
n, m, r = map(int, input().split()) #정점 수, 간선 수, 시작 정점
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) #방문 여부
depth = [-1] * (n+1) #깊이
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()
def dfs(v, d):
    visited[v] = True
    depth[v] = d
    for i in graph[v]:
        if not visited[i]:
            dfs(i, d+1)


dfs(r, 0)
for i in range(1, n+1):
    print(depth[i])