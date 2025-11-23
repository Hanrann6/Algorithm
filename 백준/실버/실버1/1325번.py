import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split()) #컴터 개수, 엣지 수
comp = [[] for _ in range(n+1)]
ans = [0] * (n+1) # 각 최대 컴퓨터 수


for i in range(m):
    a, b = map(int, input().split())
    comp[a].append(b)

def bfs(v):
    visited = [False] * (n + 1)
    que = deque()
    visited[v] = True
    que.append(v)
    while que:
        next_com = que.popleft()
        for i in comp[next_com]:
            if not visited[i]:
                visited[i] = True
                ans[i] += 1
                que.append(i)

for i in range(1, n+1):
    bfs(i)

max_num = max(ans)
for i in range(1, n+1):
    if ans[i] == max_num:
        print(i, end=" ")