'''

import sys
input = sys.stdin.readline
from collections import deque

# 노드 수, 시작, 끝, 간선 수
n, start, end, m = map(int, input().split())
graph = []
distance = [sys.maxsize] * n

# 연결
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

money = list(map(int, input().split())) # 버는 돈
new_graph = []
index_graph = [[] for _ in range(n)]

for a, b, c in graph:
    new_graph.append((a, b, c-money[b]))
    index_graph[a].append(b)

def bfs(n1, n2):
    q = deque([n1])
    visited = [False for _ in range(n)]
    visited[n1] = True

    while q:
        node = q.popleft()
        if node == n2:
            return True # 같은 사이클
        for next in index_graph[node]:
            if visited[next] == True:
                continue
            visited[next] = True
            q.append(next)
    return False


# 벨만-포드
distance[start] = money[start] # 초기화
ans = ""
for i in range(n):
    for j in range(m):
        s, e, d = new_graph[j] # 출발, 끝, 비용
        if distance[s] >= sys.maxsize:
            continue
        if distance[e] > distance[s] + d:
            distance[e] = distance[s] + d
            if i == n-1:
                if bfs(s, end): #s와 end가 같은 사이클
                    ans = "Gee" #돈 무한
                    break

if ans!="Gee":
    if distance[end] >= sys.maxsize:
        ans="gg"
    else:
        ans=-distance[end]

print(ans)

'''

import sys
input = sys.stdin.readline

n, start, end, m = map(int, input().split())
graph = {} # 그래프 저장
for i in range(m):
    a, b, c = map(int, input().split())
    if a not in graph:
        graph[a] = []
    graph[a].append((b, c))
money_list = list(map(int, input().split()))

def bellman_ford(start):
    distance_list = [-sys.maxsize] * (n + 1) # 최대 수익 리스트
    distance_list[start] = money_list[start] # start값 초기화

    for i in range(n + 100):
        for u in graph:
            for v, w in graph[u]:
                if distance_list[u] == -sys.maxsize: # 도달 불가
                    continue
                elif distance_list[u] >= sys.maxsize: # u 무한 수익 -> v 무한 수익
                    distance_list[v] = sys.maxsize
                elif distance_list[v] < distance_list[u] + money_list[v] - w:
                    distance_list[v] = distance_list[u] + money_list[v] - w
                    if i >= n - 1:
                        distance_list[v] = sys.maxsize
    return distance_list

distance = bellman_ford(start)
if distance[end] <=-sys.maxsize: # 도달 불가
    print("gg")
elif distance[end] >= sys.maxsize: # 무한 수익
    print("Gee")
else: # 최대 수익
    print(distance[end])