import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    alist.sort()
    blist.sort()
    ans=0
    count=0
    for b in blist:
        for a in range(count, n):
            if(alist[a] <= b):
                count += 1
                continue
            else:
                ans += (n-count)
                break
    print(ans)



'''
실버3, 성공
a: 1 1 3 7 8
b: 1 3 6
'''