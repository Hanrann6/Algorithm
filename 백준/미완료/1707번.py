
'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input()) #케이스 개수
# 아직 못 풀음
def bfs(v):
    visited[v] = 1
    que = deque()
    que.append(v)
    while que:
        next_N = que.popleft()
        for n in node[next_N]:
            if visited[n] == 0:
                visited[n] = 1
                que.append(n)


for _ in range(t):
    v, e = map(int, input().split()) #정점, 간선
    node = [[] for i in range(v+1)]
    visited = [0] * (v+1)
    visited[0] = 1
    a, b = 0, 0
    for k in range(e):
        a, b = map(int, input().split())
        node[a].append(b)
    bfs(a)
    if 0 in visited:
        print("YES")
    else:
        print("NO")
'''
# 책 보고 풀음
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
even = True

def dfs(v):
    global even
    visited[v] = True
    for k in node[v]:
        if not visited[k]:
            check[k] = (check[v]+1)%2
            dfs(k)
        elif check[v] == check[k]:
            even = False


for _ in range(n):
    v, e = map(int, input().split())
    node = [[] for i in range(v + 1)]
    visited = [False] * (v + 1)
    check = [0] * (v + 1)
    even = True
    for i in range(e):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)

    for i in range(1, v + 1):
        if even:
            dfs(i)
        else:
            break

    if even:
        print("YES")
    else:
        print("NO")

