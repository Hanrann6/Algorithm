import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


visited = [False] * (n+1)
parent = [0] * (n+1)

def dfs(v):
    visited[v] = True
    for i in tree[v]:
        if not visited[i]:
            parent[i] = v
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parent[i])