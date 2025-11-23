import sys
input = sys.stdin.readline
n = int(input())
wlist = [int(input()) for _ in range(n)]
wlist.sort(reverse=True) #거꾸로 정렬

ans=wlist[n-1]*n
while n > 1:
    wlist.pop()
    n -= 1
    if(wlist[n-1]*n > ans):
        ans = wlist[n - 1] * n
print(ans)

'''
sum(list)/n
50 20 15 10
'''