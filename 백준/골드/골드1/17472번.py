'''
1, 지도 정보 저장
2. dfs로 섬 구분(방문 여부 확인)
3. 길이 2 이상 에지 리스트 추가
4. 최소 신장 트리 알고리즘
'''
import heapq
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 높이, 가로
maps = []
for _ in range(n):
    a = list(map(int, input().split()))
    maps.append(a)


def dfs(i, j): # 섬 구분하기 dfs
    q = deque()
    visited[i][j] = True
    q.append([i, j])
    maps[i][j] = sNum
    while q:
        a, b = q.popleft()
        for m1, m2 in move:
            n1 = a + m1
            n2 = b + m2
            if (n1 >= 0 and n1 < n) and (n2 >= 0 and n2 < m):
                if maps[n1][n2] != 0 and not visited[n1][n2]:
                    maps[n1][n2] = sNum
                    visited[n1][n2] = True
                    q.append([n1, n2])


# 섬 구분하기
visited = [[False for _ in range(m)] for i in range(n)]
move = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 상하좌우 이동
sNum = 0 # 섬 번호

for i in range(n):
    for j in range(m):
        if maps[i][j] != 0:
            if visited[i][j] == False:
                sNum += 1
                dfs(i, j)



def Edge(i, j, now): # 다리 연결 함수
    for m1, m2 in move: # 상하좌우
        l = 0 # 길이
        n1 = i + m1
        n2 = j + m2
        while (n1 >= 0 and n1 < n) and (n2 >= 0 and n2 < m): # 범위 내에서
            if maps[n1][n2] == now: # 자기 섬이면
                break
            elif maps[n1][n2] == 0: # 바다면
                l += 1
            elif maps[n1][n2] != 0: # 다른 섬
                if l >= 2:
                    heapq.heappush(edge, (l, maps[i][j], maps[n1][n2]))
                break
            n1 += m1
            n2 += m2


# 다리 연결하기
edge = [] # 다리
for i in range(n):
    for j in range(m):
        if maps[i][j] != 0:
            now = maps[i][j] # 지금 섬 번호
            Edge(i, j, now)


def find(v):
    if v == owner[v]:
        return v
    else:
        owner[v] = find(owner[v])
        return owner[v]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        owner[b] = owner[a]

# 최소 신장 트리
owner = [i for i in range(sNum+1)]
ans = 0
cnt = 0
while edge:
    c, a, b = heapq.heappop(edge)
    if find(a) != find(b):
        union(a, b)
        ans += c
        cnt += 1


if cnt == sNum - 1:
    print(ans)
else:
    print(-1)