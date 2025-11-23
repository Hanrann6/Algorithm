import sys
input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
'''
신발끈
x1 x2 x3 x1
y1 y2 y3 y1
'''
ccw = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

if ccw > 0: # 양수면 반시계
    print(1)
elif ccw == 0:
    print(0) # 0이면 일직선
else: # 음수면 시계
    print(-1)