import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split()) # 노드 수, 에지 수
edge = []
owner = [i for i in range(v+1)]

# 에지 저장과 정렬
for i in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(edge, (c, a, b)) # 가중치, 시작, 끝

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

cnt=0
ans=0
while cnt < v-1: # v-1개까지 선택
    c, a, b = heapq.heappop(edge)
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        ans += c

print(ans)