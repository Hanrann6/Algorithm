import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 높이, 가로
n, m = map(int, input().split())
cam = []
me_x, me_y = 0, 0
for j in range(n):
    s = input().strip()
    new_s = []
    for i in range(len(s)):
        if s[i] == 'O':
            new_s.append(0)
        elif s[i] == 'X':
            new_s.append(1)
        elif s[i] == 'P': # 친구
            new_s.append(2)
        elif s[i] == 'I':
            me_x = i
            me_y = j
            new_s.append(0)
    cam.append(new_s)

visited = [[False for _ in range(m)] for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
f = [0] # 친구
def dfs(x, y):
    if x<0 or x>=m or y<0 or y>=n:
        return
    if cam[y][x] == 1: # 벽
        return
    if visited[y][x]:
        return
    else:
        visited[y][x] = True
    if cam[y][x] == 2:
        f[0] += 1
    for i in range(4):
        dfs(x + dx[i], y + dy[i])

dfs(me_x, me_y)
if f[0] == 0:
    print('TT')
else:
    print(*f)


