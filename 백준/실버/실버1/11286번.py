import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    k = int(input())
    if(k==0):
        if not heap: #비어있으면 0 출력
            print(0)
        else:
            a, b = heapq.heappop(heap)
            print(b)
    else:
        #절댓값 기준, 다음은 -+ 기준으로 저장
        heapq.heappush(heap, (abs(k), k))

# 실버 1, 성공