import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input()) #컴퓨터 쌍의 수
com = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)

def bfs(com, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in com[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(com, 1, visited)
count =0
for check in visited:
    if check:
        count += 1
print(count - 1)