import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a_list = list(map(int, input().split())) # 꺼내야함
dq = deque()

for i in range(1, n+1):
    dq.append(i)

cnt = 0
for a in a_list:
    idx = dq.index(a) # 원소의 인덱스
    l = len(dq)
    if idx == 0: # 이미 맨앞
        dq.popleft()
    elif idx <= l/2: # 앞쪽에 있으면
        for _ in range(idx):
            dq.append(dq.popleft())
            cnt += 1
        dq.popleft()
    else: # 뒤쪽에 있으면
        for _ in range(l-idx):
            dq.appendleft(dq.pop())
            cnt += 1
        dq.popleft()

print(cnt)