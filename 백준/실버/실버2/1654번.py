import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # 개수, 필요 개수
line = [int(input()) for _ in range(k)]

# 이진 탐색
ans = [] # 가능한 랜선 길이
def f(a, b):
    if b - a < 1:
        return
    min = (a + b) // 2 # min
    cnt = 0
    # 나오는 랜선 수 cnt
    for l in line:
        cnt += l//min
    if cnt < n: # 적게 나옴 -> 길이 줄임
        f(a, min)
    elif cnt >= n: # 많이 나옴 -> 저장
        if ans:
            if min == ans[-1]: # 같은 값
                return
        ans.append(min)
        f(min, b)


f(0, 2**31)
print(max(ans))