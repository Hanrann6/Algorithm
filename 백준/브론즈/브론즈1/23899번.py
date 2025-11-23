import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans=0
for i in range(n-1, -1, -1):
    if (A == B): #이거 for문 밑쪽에 뒀다가 틀림
        ans = 1
    pivot = max(A[:i+1])
    k = A.index(pivot)
    end = A[i]
    A[i] = pivot
    A[k] = end


print(ans)