import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
num.sort()
dp = []
sum=0
for i in range(n):
    sum += num[i]
    dp.append(sum)
print(dp)
'''
1 2 3 4 5
dp - [1, 3, 6, 10, 15]
'''
ans=0
for i in range(n):
    for j in range(n):
        break # 아직 못 풂