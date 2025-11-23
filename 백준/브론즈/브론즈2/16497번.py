import sys

n = int(sys.stdin.readline()) #건 수
alist = [] #대출일
blist = [] #반납일
dlist = [0] * 31 #달력
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    alist.append(a)
    blist.append(b)
k = int(sys.stdin.readline()) #책 수

for i in range(n):
    for d in range(alist[i], blist[i]):
        dlist[d] += 1

if(max(dlist) > k):
    print(0)
else:
    print(1)