import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y*100)//x #식을 이렇게 써야 맞음..
start, end = 0, 1000000000
mid = start

if(z>=99):
    print(-1)
    exit()

while start <= end:
    mid = (start + end) // 2
    x1 = x + mid
    y1 = y + mid
    z1 = (y1*100)//x1
    if (z1 > z):
        end = mid - 1
    else:
        start = mid + 1


print(start)