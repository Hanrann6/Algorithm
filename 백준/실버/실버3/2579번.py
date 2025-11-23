import sys
input = sys.stdin.readline

n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[0])
    exit()
'''
중요 !!
값이 최대가 되려면, 최대한 밟는 게 좋음
i번째 계단에 가기 위한 경우의 수는 2개뿐
i-2 -> i
i-3, i-1 -> i
'''
dp = [0 for _ in range(n+1)]

dp[1] = stair[0]
dp[2] = stair[0] + stair[1]

for i in range(3, n+1):
    dp[i] = max(dp[i-2], dp[i-3] + stair[i-2]) + stair[i-1]



print(dp[n])