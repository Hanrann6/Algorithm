import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = list(input().strip())
b = list(input().strip())
a_l = len(a)
b_l = len(b)
dp = [[0 for i in range(b_l + 1)] for j in range(a_l + 1)]
path = []

for i in range(1, a_l + 1):
    for j in range(1, b_l + 1):
        if a[i-1] == b[j-1]: # 같은 문자열일 때
            dp[i][j] = dp[i-1][j-1] + 1 # 대각선 + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 왼, 위 중 큰 수

print(dp[a_l][b_l])

def lcs(row, col):
    if row == 0 or col == 0:
        return
    if a[row-1] == b[col-1]:
        path.append(a[row-1])
        lcs(row-1, col-1)
    else:
        if dp[row-1][col] > dp[row][col-1]:
            lcs(row-1, col)
        else:
            lcs(row, col-1)

lcs(a_l, b_l)

for i in range(len(path)-1, -1, -1):
    print(path.pop(i), end='')

print()
