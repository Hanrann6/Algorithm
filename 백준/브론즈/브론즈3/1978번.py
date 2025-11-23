import sys
input = sys.stdin.readline

n = int(input())
ns = list(map(int, input().split()))
ans = 0

def isS(n):
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True


for i in ns:
    if i == 1:
        continue
    if isS(i):
        ans += 1

print(ans)