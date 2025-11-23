import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
le = [0] * n # 왼쪽 연속 합
ri = [0] * n # 오른쪽 연속 합
le[0] = nums[0]
ri[n-1] = nums[n-1]
ans = le[0]

# 왼쪽 합 리스트
for i in range(1, n):
    le[i] = max(nums[i], le[i-1] + nums[i])
    ans = max(ans, le[i])

# 오른쪽 합 리스트
for i in range(n-2, -1, -1):
    ri[i] = max(nums[i], ri[i+1] + nums[i])

for i in range(1, n-1):
    t = le[i-1] + ri[i+1]
    ans = max(ans, t)

print(ans)
