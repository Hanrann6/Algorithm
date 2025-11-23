import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
dp = [[[0 for i in range(101)] for j in range(101)] for k in range(101)]
dp[1][1][1] = 1
mm = 1000000007

for i in range(2, n+1):
    for j in range(1, l+1):
        for k in range(1, r+1):
            dp[i][j][k] = (dp[i-1][j][k]*(i-2) + (dp[i-1][j][k-1] + dp[i-1][j-1][k])) % mm

print(dp[n][l][r])