import sys
from collections import deque
input = sys.stdin.readline

#도시 개수, 도로 개수, 거리 정보, 출발지
n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]
ans = []
visited = [-1] * (n+1)

#도로 정보 저장
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

def bfs(x):
    que = deque()
    que.append(x)
    visited[x] += 1
    while que:
        next_City = que.popleft()
        for i in city[next_City]:
            if visited[i] == -1:
                visited[i] = visited[next_City] + 1
                que.append(i)


bfs(x)

for i in range(n+1):
    if visited[i] == k:
        ans.append(i)

if not ans:
    print(-1)
else:
    ans.sort()
    print("\n".join(map(str, ans)))