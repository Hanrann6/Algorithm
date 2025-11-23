'''
A<B<C -> C-B
A<C<B
B<A<C
B<C<A
C<A<B
C<B<A
책 보고 함
'''

import sys
from collections import deque
input = sys.stdin.readline

sender = [0, 0, 1, 1, 2, 2]
receiver = [1, 2, 0, 2, 0, 1]
now = list(map(int, input().split()))
visited = [[False for j in range(201)] for i in range(201)]
answer = [False] * 201

def bfs():
    que = deque()
    que.append((0, 0))
    visited[0][0] = True
    answer[now[2]] = True
    while que:
        now_N = que.popleft()
        a = now_N[0]
        b = now_N[1]
        c = now[2] - a - b # c는 전체 물의 양에서 a와 b를 뺀 것
        for k in range(6): #6가지 경우의 수
            next = [a, b, c]
            next[receiver[k]] += next[sender[k]]
            next[sender[k]] = 0
            if next[receiver[k]] > now[receiver[k]]: #물이 넘칠 때
                # 초과하는 만큼 다시 이전 물통에 넣어 주기
                next[sender[k]] = next[receiver[k]] - now[receiver[k]]
                next[receiver[k]] = now[receiver[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                que.append((next[0], next[1]))
                if next[0] == 0: #a의 물의 양이 0일 때 c의 물의 무게를 정답에 저장
                    answer[next[2]] = True

bfs()

for i in range(len(answer)):
    if answer[i]:
        print(i, end = ' ')