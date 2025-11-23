import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
l = []
for i in range(n):
    s = list(map(int, input().split()))
    l.extend(s)


max_l = max(l)
min_l = min(l)
h=min_l
time = sys.maxsize

# 더 복잡도 줄이려면 높이당 개수가 들은 리스트 사용
for mid in range(min_l, max_l+1):
    put = 0 # 채우는 개수
    pull = 0 # 깎는 개수
    for j in l:
        if j-mid > 0:  # 잘라야 함
            pull += (j-mid)
        elif j-mid < 0:  # 채워야 함
            put += (mid-j)
    if b - put + pull < 0: # 블록 부족
        break
    else:
        if pull*2 + put <= time:
            time = pull*2 + put
            h = mid

print(time, h)