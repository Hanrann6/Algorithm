import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
card = PriorityQueue()
for _ in range(n):
    card.put(int(input())) #우선순위 큐는 put 사용

cnt=0
for _ in range(n-1):
    a = card.get() #우선순위 큐는 get 사용
    b = card.get()
    cnt += (a + b)
    card.put(a+b)

print(cnt)