import sys
import math
input = sys.stdin.readline
# 에라토스테네스의 체
a, b = map(int, input().split())
sq = int(math.sqrt(b)) + 1
li = list(range(0, sq))
li[1] = 0
for i in range(2, sq):
    if i == 0: continue
    k = i * 2
    if k > sq: continue
    else:
        while k <= (sq-1):
            if li[k] != 0:
                li[k] = 0
            k += i

cnt=0
for i in li:
    if i == 0:
        continue
    num = i**2
    while num <= b:
        if num >= a:
            cnt += 1
        num *= i

print(cnt)