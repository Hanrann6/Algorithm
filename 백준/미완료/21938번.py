import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split()) #가로, 세로
color = [[] for _ in range(m)]
visited = [[False]*m for _ in range(m)]
for i in range(m):
    c = list(map(int, input().split()))
    for j in range(0, n*3, 3):
        red, green, blue = c[j], c[j+1], c[j+2]
        avg = (red + green + blue) / 3
        color[i].append(avg)

t = int(input()) #경계값
def bfs(v, color, t):
    queue = deque[v]
    visited[v] = True
    while queue:
        v = queue.popleft()
        # for i in color[v]:
        #     if dd

#풀다 말음
print(visited)