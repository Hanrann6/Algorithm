# 1064번 - 실버 4
import sys
import math

xy = list(map(int, sys.stdin.readline().split()))
if (xy[2] - xy[0]) == 0 and (xy[4] - xy[2]) == 0:
    m1 = 0
    m2 = 0
elif (xy[2] - xy[0]) == 0 or (xy[4] - xy[2]) == 0:
    m1 = 0
    m2 = 1
else:
    m1 = (xy[3] - xy[1]) / (xy[2] - xy[0])
    m2 = (xy[5] - xy[3]) / (xy[4] - xy[2])

if m1 == m2:
    print(-1.0)
else: #제곱근 사용
    l1 = math.sqrt((xy[2] - xy[0]) ** 2 + (xy[3] - xy[1]) ** 2)
    l2 = math.sqrt((xy[4] - xy[2]) ** 2 + (xy[5] - xy[3]) ** 2)
    l3 = math.sqrt((xy[4] - xy[0]) ** 2 + (xy[5] - xy[1]) ** 2)
    len1 = l1 * 2 + l2 * 2
    len2 = l2 * 2 + l3 * 2
    len3 = l1 * 2 + l3 * 2
    len_list = [len1, len2, len3]
    print(max(len_list) - min(len_list))