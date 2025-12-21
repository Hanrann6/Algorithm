import sys

n = int(input()) # 설탕
k = sys.maxsize
dp = [k for i in range(n+1)]
dp[0] = 0
dp[1] = k
dp[2] = k
dp[3] = 1

for i in range(5, n+1):
    a, b = k, k
    if dp[i-5] != k:
        a = dp[i-5] + 1
    elif dp[i-3] != k:
        b = dp[i-3] + 1
    dp[i] = min(a, b)

if dp[n] == k:
    print(-1)
else:
    print(dp[n])