import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split()) # 사람, 번째
people = deque()
for i in range(1, n+1):
    people.append(i)

i = 1
ans = []
while people:
    cnt = i % k # k번째 사람이면
    i += 1
    if cnt == 0:
        ans.append(people.popleft())
    else:
        people.append(people.popleft())

print('<', end='')
for a in range(len(ans)):
    print(ans[a], end='')
    if a != len(ans)-1:
        print(', ', end='')
    else:
        print('>', end='')