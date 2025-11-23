import sys
input = sys.stdin.readline

t = int(input()) # 테케 수
for _ in range(t):
    h, w, n = map(int, input().split()) #층, 방, 손님
    xx = n//h + 1 # 머물 호수
    yy = n%h # 머물 층
    if yy == 0: # 꼭대기 층이면
        yy = h
        xx -= 1
    if xx < 10:
        xxs = "0" + str(xx)
        print(str(yy) + xxs)
    else:
        print(str(yy) + str(xx))
