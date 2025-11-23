import heapq
import sys
input = sys.stdin.readline

t = int(input())
tlist = []
for _ in range(t):
    tlist.append(int(input()))

n = max(tlist)
dp = [0 for _ in range(4)]
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(3, n):
    dp.append(dp[i-1] + dp[i-2])

for i in range(t):
    print(dp[tlist[i]])