import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input()) # tk

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if (x < 0) or (x >= m) or (y < 0) or (y >= n):
        return
    if ground[y][x] == 0 or visited[y][x]:
        return
    visited[y][x] = True
    for i in range(4):
        dfs(x + dx[i], y + dy[i])


# 그래프 개수 구하는 문제
for _ in range(t):
    m, n, k = map(int, input().split())
    ground = [[0 for i in range(m)] for j in range(n)]
    # 가로 m, 세로 n
    # 농장 저장
    for _ in range(k):
        x, y = map(int, input().split())
        ground[y][x] = 1
    cnt = 0
    visited = [[False for i in range(m)] for j in range(n)]
    for i in range(n): # 세로
        for j in range(m): # 가로
            if ground[i][j] == 1 and not visited[i][j]:
                dfs(j, i)
                cnt += 1
    print(cnt)


