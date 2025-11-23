import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()

def search(target, a):
    start, end = 0, n-1 # 인덱스
    while start <= end:
        mid = (start + end) // 2
        if a[mid] > target:
            end = mid - 1
        elif a[mid] == target:
            return True
        else:
            start = mid + 1
    return False


cnt = 0
for i in a:
    b = x-i
    if b <= 0:
        continue
    if search(b, a):
        cnt += 1

print(cnt//2)