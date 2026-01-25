import sys
input = sys.stdin.readline

n = int(input())
san = set(map(int, input().split()))
m = int(input())
mn = list(map(int, input().split()))
ans = []
for i in mn:
    if(i in san):
        ans.append(1)
    else:
        ans.append(0)

print(*ans)