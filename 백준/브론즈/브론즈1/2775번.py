import sys
input = sys.stdin.readline

n = int(input()) # 테케 수
dp = [[0 for _ in range(15)] for i in range(15)] # 최대 14층/14호

for i in range(15): # 테이블 초기화
    dp[i][1], dp[0][i] = 1, i

for i in range(1, 15):
    for j in range(2 ,15):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for _ in range(n):
    a = int(input()) # 층
    b = int(input()) # 호
    print(dp[a][b])