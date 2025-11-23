#1051번 - 실버 3
import sys
n, m = map(int, sys.stdin.readline().split())
li = [[0]*m for _ in range(n)]
for i in range(n):
    num = sys.stdin.readline()
    for k in range(m):
        number = int(num[k])
        li[i][k] = number

sq = min(n, m)
len_list = [0]
for i in range(n):
    for k in range(m):
        len = 0
        for _ in range(sq-1):
            len += 1
            if((i+len) > (n-1) or (k+len) > (m-1)):
                break
            if(li[i][k] == li[i][k+len] == li[i+len][k] == li[i+len][k+len]):
                len_list.append(len)

print((max(len_list)+1)*(max(len_list)+1))