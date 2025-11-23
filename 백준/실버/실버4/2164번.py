import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
for i in range(1, n+1): #카드 세팅
    queue.append(i)

for i in range(1, n):
    queue.popleft() #윗장 버림
    queue.append(queue.popleft()) #윗장 아래에 깔기

print(queue.popleft())

#실버 4. 성공