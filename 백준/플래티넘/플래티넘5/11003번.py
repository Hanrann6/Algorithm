import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
deq = deque()
now = list(map(int, input().split()))

for i in range(n):
    while deq and deq[-1][0] > now[i]:
        deq.pop()
    deq.append((now[i], i))
    if(deq[0][1] <= i - l):
        deq.popleft()
    print(deq[0][0], end=' ')
'''
num = list(map(int, input().split()))
#0부터 최솟값 리스트 생성
mlist = [num[0]]
for i in range(1, n):
    if(mlist[i-1] > num[i]):
        mlist.append(num[i])
    else:
        mlist.append(mlist[i-1])
#부분 최솟값 리스트 생성
min2 = mlist[l-1]
min_list = []
k=0
if(l > 1): #인덱스가 0보다 작을 경우
    min_list.extend(mlist[:l])
for i in range(l, n):
    if (min2 == num[i - l]): #사라지는 값이 최솟값이였을 때
            min2 = min(num[i-l+1:i+1]) #이부분 시간을 줄여야 하나?
    if (num[i] < min2):  # 다음 값이 더 작으면
            min2 = num[i]
    min_list.append(min2)

print(*min_list)


D = l이 3인 경우 -> a3-a5, a4-a6 ...
구간이 l인 구간의 최솟값 구하기
1 3 4 2 5
런타임 에러
'''