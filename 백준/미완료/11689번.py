import sys
import math
n = int(sys.stdin.readline())
ans = n

for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        ans -= ans/i
        while n%i == 0:
            n /= i

if n > 1:
    ans -= ans/n
print(int(ans))
# 책 베낌