import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input()) #도시 개수
m = int(input()) #여행 경로 데이터

city = [i for i in range(n+1)] #도시
host = [i for i in range(n+1)] #주인

def union(a, b): #합체
    p = find(a)
    q = find(b)
    if(p == q):
        return
    else:
        host[q] = p

def find(a): #주인 원소 찾기
    if (host[a] == a):
        return a
    else:
        host[a] = find(host[a])
        return host[a]

#도시 연결하기
for i in range(n):
    road = list(map(int, input().split())) #연결 정보
    for j in range(n):
        if road[j] == 1:
            union(i+1, j+1)

trab = list(map(int, input().split())) #여행 도시
first = find(trab[0])
for i in trab:
    second = find(i)
    if (first == second):
        continue
    else:
        print('NO')
        exit()

print('YES')
