import sys
sys.setrecursionlimit(10000) #이거 없으면 런타임 에러. RecursionError
input = sys.stdin.readline
n, m = map(int, input().split())
dfs = [[] for _ in range(n+1)]
visit = [False] * (n+1) #방문 기록. 0이 미방문
ans=0
for _ in range(m):
    a, b = map(int, input().split())
    dfs[a].append(b) #방향성 없는 그래프
    dfs[b].append(a)


def dfs_f(s):
    visit[s] = True
    for k in dfs[s]:
        if visit[k] == 0:
            dfs_f(k)

for s in range(1, n+1):
    if not visit[s]:
        ans += 1
        dfs_f(s)

print(ans)
#dfs 문젠데 거의 책 배낌