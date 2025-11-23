import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = num[0]
#부분합 리스트 생성
for i in range(1, n):
    dp[i] = dp[i-1] + num[i]

count = [0] * m #나머지 배열
ans = 0

# 나머지가 같은 구간합은 (count[i]-count[j])%m이 0이다!
for i in range(n):
    mod = dp[i] % m
    if(mod == 0):
        ans += 1
    count[mod] += 1

for i in range(m):
    if(count[i] > 1):
        ans += (count[i] * (count[i] - 1) // 2)
print(ans)

#골드 3, 거의 답 봄, 성공