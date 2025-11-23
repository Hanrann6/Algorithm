import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split()) # a, b
x3, y3, x4, y4 = map(int, input().split()) # c, d


'''
A-B 선분, C-D 선분일 때
A-B-C ccw * A-B-D ccw,
C-D-A ccw * C-D-B ccw가 모두 음수면 교차함 
'''

def ccw(x1,y1, x2, y2, x3, y3):
    ccw = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    return ccw


t1 = ccw(x1, y1, x2, y2, x3, y3) # a, b, c
t2 = ccw(x1, y1, x2, y2, x4, y4) # a, b, d
t3 = ccw(x3, y3, x4, y4, x1, y1) # c, d, a
t4 = ccw(x3, y3, x4, y4, x2, y2) # c, d, b

test1 = t1 * t2
test2 = t3 * t4

if test1 == 0 and test2 == 0: # 일직선
    # 겹침
    if (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2)) \
            and (min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)):
        print(1)
    else: # 겹침
        print(0)
elif test1 <= 0 and test2 <= 0: # 교차. 한 점이 겹칠수도
    print(1)
else: # 교차 안 함
    print(0)
