import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, input().split()))
sum_n = sum(num[:k])
max=sum_n
for i in range(n-k):
    sum_n -= num[i]
    sum_n += num[i+k]
    if(max < sum_n):
        max = sum_n
print(max)