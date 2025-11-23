# 에라토스테네스의 체 원리
import sys
import math
input = sys.stdin.readline
m, n = map(int, input().split())
li = [0] * (n+1)
for i in range(2, n+1): li[i] = i

li[1] = 0
for i in range(2, int(math.sqrt(n))+1):
    if li[i] == 0:
        continue
    else:
        if i * 2 > n:
            continue
        else:
            k = i * 2
            while k <= n:
                if li[k] != 0:
                    li[k] = 0
                k += i


for i in li:
    if i != 0 and i >= m:
        print(i)
