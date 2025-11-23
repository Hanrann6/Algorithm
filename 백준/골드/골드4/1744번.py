import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
p_num = PriorityQueue() #양수
m_num = PriorityQueue() #음수
one, zero = 0, 0
for _ in range(n):
    k = int(input())
    if k == 0:
        zero += 1
    elif k == 1:
        one += 1
    elif k >= 2:
        p_num.put(k * -1) #오름차순 정렬
    else:
        m_num.put(k)

ans=0
while p_num.qsize() >= 2: #우선순위 큐의 길이는 qsize()
    a = p_num.get()
    b = p_num.get()
    ans += (a*b)

if p_num.qsize() > 0:
    ans += p_num.get() * -1
ans += one

while m_num.qsize() >= 2:
    a = m_num.get()
    b = m_num.get()
    ans += (a*b)


if m_num.qsize() > 0 and zero == 0:
    ans += m_num.get()


print(ans)

'''
양수끼리는 큰 수끼리 곱해야 한다
음수끼리는 작은 수끼리 곱해야 한다
1은 곱하는 것보다 더하는 게 이득
0은 남은 음수에 곱해줌
'''