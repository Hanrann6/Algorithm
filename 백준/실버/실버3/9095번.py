import sys
input = sys.stdin.readline

t = int(input())
dp = [0 for _ in range(11)]

dp[1] = 1
dp[2] = 2 # 2, 1+1
dp[3] = 4 # 3, 1+1+1, 1+2, 2+1
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


for _ in range(t):
    n = int(input())
    print(dp[n])
