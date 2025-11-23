import sys
import math
input = sys.stdin.readline

t = int(input()) # 테케 수
for _ in range(t):
    n, m = map(int, input().split())
    print(math.comb(m, n)) # m개 다리에서 n 다리를 선택