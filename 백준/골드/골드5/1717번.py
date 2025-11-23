import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split()) #원소 개수, 질문 개수

node = [i for i in range(n+1)] #원소
top = [i for i in range(n+1)] #주인

def union(a, b): #합체
    p = find(a)
    q = find(b)
    if(p == q):
        return
    else:
        top[q] = p

def find(a): #주인 원소 찾기
    if (top[a] == a):
        return a
    else:
        top[a] = find(top[a])
        return top[a]

for _ in range(m):
    is_0, a, b = map(int, input().split())
    if is_0 == 0:
        union(a, b)
    else:
        if(find(a) == find(b)):
            print("YES")
        else:
            print("NO")


