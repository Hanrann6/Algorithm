import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]

if n == 1:
    print(1)
    exit()

dp[1] = 1
dp[2] = 3

'''
dp[i]에 도달하는 경우의 수
- 1칸 전에서 +1
- 2칸 전에서 +2
'''

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]*2

print(dp[n]%10007)