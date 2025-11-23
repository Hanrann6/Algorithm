import sys
import heapq
heap = []
n =  sys.stdin.readline().strip()
for i in range(len(n)):
    heapq.heappush(heap, -(int(n[i])))

for _ in range(len(n)):
    print(-(heapq.heappop(heap)), end='')

#실버 5. 성공