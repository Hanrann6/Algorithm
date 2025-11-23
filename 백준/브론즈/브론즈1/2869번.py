import sys
a, b, v = map(int, sys.stdin.readline().split())
c = a - b
day=0
hi =0
if(a >= v):
    day = 1
else:
    ell = v - a #낮 제외 남은 높이
    day = ell // c
    hi = day * c
    for _ in range(2):
        hi += a
        if(hi >= v):
            day += 1
            break
        hi -= b
        day += 1

print(day)

'''
3 2 5 -> 3일 낮
2 1 5 -> 4일 낮
3 1 10 -> 5일 낮
4 2 13 -> 6일가고 + 낮

'''