import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())

maze = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)] #방문 여부 표시

def check_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

# print(maze)

q = deque()
q.append([0,0,1])
visited[0][0] = True

dx = [1, -1, 0, 0] #오른쪽, 왼쪽
dy = [0, 0, 1, -1] #위아래

while q:
    a,b, d = q.popleft() #x자리, y자리, 거리
    if a==n-1 and b==m-1: #도착
        print(d)
        break
    if maze[a][b] ==0 : #이동할 수 없으면
        continue
    for x, y in zip(dx, dy): #튜플화해서 좌우상하
        cur_a = a+x #현재 x자리
        cur_b = b+y #현재 y자리

        #범위 안에 있고, 이동 가능하고, 방문 안 했으면
        if check_range(cur_a, cur_b) == True \
                and maze[cur_a][cur_b] ==1 \
                and visited[cur_a][cur_b] == False:
            q.append([cur_a, cur_b, d+1])
            visited[cur_a][cur_b] = True #방문

#답 베낌
