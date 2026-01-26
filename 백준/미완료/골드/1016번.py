# import sys
# import math
# input = sys.stdin.readline
# n, m = map(int, input().split())
# li = list(range(n, m+1))
#
# for i in range(2, int(math.sqrt(m)) + 1):
#     if i >= n:
#         if li[i-n] == 0:
#             continue
#     num = i**2
#     for k in range(num, m, num):
#         if k-n >= 0:
#             li[k - n] = 0
#
# cnt=0
# for i in li:
#     if i != 0:
#         cnt += 1
# print(cnt)
#시간 초과

# 아래는 배낌
min, max = map(int, input().split())

answer = max - min + 1
divisibleByTheSquare = [False] * (max-min+1)

for i in range(2, int(max**0.5+1)):
    square = i**2
    for j in range((((min-1)//square)+1)*square, max+1, square):
        if not divisibleByTheSquare[j-min] :
            divisibleByTheSquare[j-min] = True
            answer -= 1
print(answer)