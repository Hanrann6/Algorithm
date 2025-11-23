import math
import sys
input = sys.stdin.readline

# 제곱근 구할 때 math.sqrt(n)는 부동소수점 오차로 틀림
n = int(input())

# 이분 탐색
# n보다 큰 최소 q^2 찾기
def search(n):
    start, end = 0, 2**32
    while start <= end:
        mid = (start + end) // 2
        if mid**2 < n:
            start = mid + 1
        else:
            end = mid - 1
    return start

print(search(n))