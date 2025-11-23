import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m=map(int,input().split())

friend=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    friend[a].append(b) #무방향 그래프
    friend[b].append(a)

def dfs(x,visited,cnt): #dfs로 탐색. cnt는 친구 수
    visited[x]=True
    if cnt==4: #이미 4명이면
        return 1

    for i in friend[x]:
        if not visited[i]: #방문 안했으면 계속 들어감
            if dfs(i,visited,cnt+1):
                return 1
    visited[x]=False
    return 0


for i in range(n): #각 노드에서 끝과 연결되는지 확인
    visited=[False for _ in range(n)]

    if dfs(i,visited,0): #존재하면
        print(1)
        exit()
print(0)

#답 베낌