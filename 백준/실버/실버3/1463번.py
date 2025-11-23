import sys
input = sys.stdin.readline

n = int(input())
dp = [10**6] * (n+1) # 0은 안 쓰이니까 n+1
dp[1] = 0
dp[2] = 1

for i in range(3, n+1):
    i1, i2, i3 = i, i, i
    if i1 % 3 == 0:
        i1 //= 3
    if i2 % 2 == 0:
        i2 //= 2
    i3 -= 1
    dp[i] = min(dp[i1], dp[i2], dp[i3]) + 1

print(dp[n])
# 런타임 에러