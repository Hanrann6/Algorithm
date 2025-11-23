import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
dp = [[1]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] # i개, j개로 만들 수 있는 문자열 수

if dp[n][m] < k: # k 가능 범위 넘으면
    print("-1")
else:
    strg = ""
    while True: # k번째 문자열
        if n == 0 or m == 0:
            strg += "a" * n
            strg += "z" * m
            break
        flag = dp[n-1][m]
        if flag >= k:
            strg += "a"
            n -= 1
        else:
            strg += "z"
            m -= 1
            k -= flag
    print(strg)