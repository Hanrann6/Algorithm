import sys
input = sys.stdin.readline

n = int(input())
# 계단 높이 10
dp = [[0 for i in range(11)] for j in range(n+1)]

# 길이 1일 때 경우의 수 = 1
for i in range(1, 10):
    dp[1][i] = 1

# 양끝 높이 제약
for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    # 나머지 단계는 자신 앞뒤 단계
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

ans = 0
for i in range(10):
    ans = (ans + dp[n][i]) % 1000000000

print(ans)