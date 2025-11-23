import sys
input = sys.stdin.readline
n = int(input())
per = list(map(int, input().split()))

#삽입 정렬
for i in range(1, n):
    key = per[i]
    k = i-1
    while (k >= 0) and (per[k] > key):
        per[k+1] = per[k]
        k -= 1
    per[k+1] = key

slist = [per[0]]
#합배열
for i in range(n-1):
    slist.append(slist[i] + per[i+1])
print(sum(slist))

'''
import sys
input = sys.stdin.readline
n = int(input())
per = list(map(int, input().split()))

per.sort() #그냥 정렬

slist = [per[0]]
#합배열
for i in range(n-1):
    slist.append(slist[i] + per[i+1])
print(sum(slist))
'''
