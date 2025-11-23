import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
start, end = 1, k
ans = start
# k번째 수 -> x보다 작은 수가 k개 이상 있는지
# x // i의 개수들의 합
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, n+1):
        count += min(mid//i, n) #최대 n개이므로
    if count < k:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid

print(ans)

'''
#그냥 해보면 - 메모리 초과
import sys
import heapq
input = sys.stdin.readline
n = int(input())
k = int(input())
heap = []

for i in range(1, n+1):
    for j in range(1, n+1):
        heapq.heappush(heap, i*j)

for _ in range(k):
    ans = heapq.heappop(heap)

print(ans)
'''

'''
n = 4일 때
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16
=> 1 2 2 3 3 4 4 4 6 6 8 8 9 12 12 16
'''