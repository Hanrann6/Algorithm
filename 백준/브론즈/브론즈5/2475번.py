import sys
input = sys.stdin.readline

s = list(map(int, input().split()))
sum = 0
for i in s:
    sum += i*i

print(sum % 10)