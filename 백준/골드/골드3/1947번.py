n = int(input())
dp = [0]*1000001 # i명 선물 교환하는 방법의 수
dp[1] = 0
dp[2] = 1

for i in range(3, n+1):
    dp[i] = (i-1)*(dp[i-1]+dp[i-2])%1000000000 # 완전 순열

print(dp[n])