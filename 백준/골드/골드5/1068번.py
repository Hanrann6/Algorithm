import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
d_node = int(input()) # 삭제 노드
tree = [[] for _ in range(n+1)]
root = 0


for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        tree[i].append(parent[i])
        tree[parent[i]].append(i)


visited = [False] * (n+1)
ans = 0

def dfs(v):
    global ans
    visited[v] = True
    child = 0 # 자식 노드 개수
    for i in tree[v]:
        if not visited[i] and (i != d_node):
            child += 1
            dfs(i)
    if child == 0: # 리프 노드
        ans += 1

if d_node == root:
    print(0)
else:
    dfs(root)
    print(ans)