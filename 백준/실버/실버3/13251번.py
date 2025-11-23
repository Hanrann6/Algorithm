import math
import sys
input = sys.stdin.readline

M = int(input()) # 색 종류
color_counts = list(map(int, input().split())) # 색깔별 조약돌 수
K = int(input()) # 뽑을 조약돌 수
N = sum(color_counts) # 전체 조약돌 수

total_cases = math.comb(N, K) # n개 중 k를 뽑는 경우의 수 nCk
favorable = 0

for c in color_counts:
    if c >= K:
        favorable += math.comb(c, K) # 특정 색에서 뽑는 경우

prob = favorable / total_cases
print(prob)
