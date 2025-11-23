import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
que = []
ans = [-1]*n
for i in range(n):
    while(que and num[i] > num[que[-1]]):
        ans[que.pop()] = num[i]
    que.append(i) #인덱스를 저장
print(*ans)
'''
골드 4. 거의 책보고 통과
# 시간초과
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
num = deque(map(int, input().split()))
ans = []

#오른쪽부터 최댓값 리스트
mlist = [num[n-1]]
for i in range(n-1):
    if(mlist[i] < num[n-i-2]):
        mlist.append(num[n-i-2])
    else:
        mlist.append(mlist[i])
mlist.reverse()

for i in range(n-1):
    p = num[i]
    if(p > mlist[i+1]):
        ans.append(-1)
        continue
    k = i
    count = num[k + 1]
    while(count < p):
         count = num[k+1]
         k += 1
    ans.append(count)
ans.append(-1)
print(*ans)

'''