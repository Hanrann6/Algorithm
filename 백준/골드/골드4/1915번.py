import sys
input = sys.stdin.readline
dp = [[0 for i in range(1001)] for j in range(1001)]
n, m = map(int, input().split())
max=0

for i in range(0, n):
    nums = list(input())
    for j in range(0, m):
        dp[i][j] = int(nums[j])
        if dp[i][j] == 1 and j>0 and i>0:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + dp[i][j] # 점화식
        if max < dp[i][j]:
            max = dp[i][j]

print(max**2)
