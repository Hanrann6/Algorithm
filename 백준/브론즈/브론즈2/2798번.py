import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

tot = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n): # i+2가 아니라 j+1임!!
            if nums[i] + nums[j] + nums[k] == m:
                print(m)
                exit()
            elif (nums[i] + nums[j] + nums[k] > m):
                continue
            elif(tot < nums[i] + nums[j] + nums[k]):
                tot = nums[i] + nums[j] + nums[k]

print(tot)