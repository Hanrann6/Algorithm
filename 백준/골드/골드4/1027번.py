import sys
input = sys.stdin.readline

n = int(input())
building = list(map(int, input().split())) # 인덱스가 x축
see = [0 for _ in range(n)] # 보이는 건물 수. 양옆
dp = [[0 for i in range(n)] for j in range(n)] #i -> j 기울기

# 왼쪽 -> 오른쪽 기울기 dp
for i in range(n):
    for j in range(i+1, n):
        dp[i][j] = (building[j] - building[i])/(j-i)


for i in range(n):
    # 앞쪽
    front = -sys.maxsize
    for j in range(i+1, n):
        a = dp[i][j]
        if front < a:
            see[i] += 1
            front = a
    # 뒤쪽
    back = sys.maxsize
    for j in range(i-1, -1, -1):
        b = dp[j][i]
        if back > b:
            see[i] += 1
            back = b


print(max(see))
