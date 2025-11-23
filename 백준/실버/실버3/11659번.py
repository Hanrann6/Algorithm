import sys
n, m = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
dp = [0]

#부분합 리스트 생성
for i in range(1, n+1):
    a = dp[i-1] + num_list[i-1]
    dp.append(a)

#부분합 계산
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(dp[y] - dp[x-1])

#실버 3, 성공