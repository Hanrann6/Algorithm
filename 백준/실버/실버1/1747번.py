import sys
import math
input = sys.stdin.readline
n = int(input())
sq = int(math.sqrt(10000001)) + 1
li = list(range(0, 10000001))
li[1] = 0

# 숫자의 배수를 제거
for i in range(2, sq):
    if li[i] == 0: continue
    for k in range(i*2, 10000001, i):
        li[k] = 0

# 팰린드롬 숫자인지 확인
def pel(n):
    s = list(str(n))
    m = int(len(s) / 2)
    if s[:m] == s[-1:-m - 1:-1]:
        return True
    return False

for i in li:
    if i != 0 and i >= n and pel(i):
        print(i)
        exit()
