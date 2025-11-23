import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = [] #힙 사용해서 정렬해보기

for _ in range(n):
    k = int(input())
    heapq.heappush(heap, k)

for _ in range(n):
    print(heapq.heappop(heap))
# print('\n'.join(map(str, heap))) heap 자체가 정렬x
'''
import sys
n = int(sys.stdin.readline())
mlist = []
for _ in range(n):
    k = int(sys.stdin.readline())
    mlist.append(k)

mlist.sort() #list 정렬하기
for i in mlist:
    print(i)
'''