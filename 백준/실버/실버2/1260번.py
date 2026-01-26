'''
#답 베낌
N,M,V = map(int,input().split())

#2차원 행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1 #1이 '존재' 표시

#방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

#dfs 함수
def dfs(V):
    visited1[V] = 1 #방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0: #연결이 존재하고 방문 안 했으면
            dfs(i)

#bfs 함수
def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)
'''


import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False for _ in range(n+1)]
d_ans = [] # dfs 결과
b_ans = [] # bfs 결과

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 인접행렬 2차원 형식에선 정렬이 필요없지만, 인접 리스트에선 필요
for i in range(1, n+1):
    graph[i].sort()

def dfs(node): # 깊이 우선 탐색
    visited[node] = True
    d_ans.append(node)
    for n in graph[node]:
        if not visited[n]:
            dfs(n)


def bfs(node): # 너비 우선 탐색
    visited2[node] = True
    dq = deque([node])
    while dq:
        ns = dq.popleft()
        b_ans.append(ns)
        for next in graph[ns]:
            if not visited2[next]:
                visited2[next] = True
                dq.append(next)



dfs(v)
print(*d_ans)

visited2 = [False for _ in range(n + 1)]
bfs(v)
print(*b_ans)